
# coding: utf-8

# In[ ]:


from pylsl import StreamInlet, resolve_stream
import numpy as np
import scipy.signal as scisig
import matplotlib.pyplot as plt
import time
from Network import Network
from json_encoder import JsonEncoder
from preprocess import apply_filter
from matplotlib.patches import Circle
from scipy.io import loadmat

import pandas as pd
import glob
import os
import json
import pprint
import csv
import _pickle as cPickle

import tensorflow as tf
# from keras.backend import tensorflow_backend
# config = tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))
# session = tf.Session(config=config)
# tensorflow_backend.set_session(session)

import keras
import keras.callbacks
import keras.backend.tensorflow_backend as KTF

pp = pprint.PrettyPrinter(indent=4)


# In[ ]:


# os.chdir(os.path.dirname(os.path.abspath(__file__)))
home_path = os.getcwd()

config_list = json.load(open(os.path.join(home_path,'config_list.json'),'r'))

config = {}
config['home_path']= home_path

config['label_set_index']= 'easy'
config['label_set']= config_list['label_sets'][config['label_set_index']]

config['model_type']='CNN2'
config['time_window'] = 100
config['input_len']=5
config['output_len']= config['label_set']['num_label']
config['input_shape']=(config['time_window'],config['input_len'])

config['batch_size']= 128
config['loss']= 'categorical_crossentropy'
config['n_epochs']= 4
config['test_rate']=0.1
config['Fs'] = 500

# In[ ]:


config['load']='whole'

figsize = (20,12)
ymin, ymax = 0, 1
max_display_size = 1000
num_output= config['output_len']
pause_time = 0.00000001
DEBUG=True
PRED_NORM=True

old_session = KTF.get_session()
with tf.Graph().as_default():
    session = tf.Session('')
    KTF.set_session(session)
    net = Network(config)
    net.load('saved_models/20171221-065527')

    if not DEBUG:
        print("looking for an EEG stream...")
        streams = resolve_stream('type', 'EEG')
        print("detect {} EEG streams!".format(len(streams)))
        inlet = StreamInlet(streams[0],max_buflen=360, max_chunklen=100, recover=True)

    
    fig = plt.figure(figsize=figsize)
    plt.ion()

    ydata = np.zeros((max_display_size,num_output),dtype=np.float32)
    ax1=fig.add_subplot(3,1,1)
    line = [ax1.plot(ydata[:,j],label='output {}'.format(config['label_set']['num2label'][str(j)])) for j in range(num_output)]
    ax1.set_ylim([ymin, ymax])
    ax1.legend(loc='lower left')
    
    ax2=fig.add_subplot(3,1,2)
    ax2.set_aspect('equal')
    circle = Circle((0, 0), 1)
    ax2.add_artist(circle)
    ax2.set_xlim([-1, 1])
    ax2.set_ylim([-1, 1])
    
    ax3=fig.add_subplot(3,1,3)
    ydata_freq = np.zeros((config['time_window'],len(config_list['freq_bands'].keys())),dtype=np.float32)
    line_freq = [ax3.plot(ydata_freq[:,j],label='{}'.format(freq)) for j,freq in enumerate(config_list['freq_bands'].keys())]
    if DEBUG:
        ax3.set_ylim([-5, 5])
    else:
        ax3.set_ylim([-0.1, 0.1])
    ax3.legend(loc='lower left')

    if DEBUG:
        fig1 = plt.figure(figsize=(8,2))
        ydata_true_label = np.zeros((max_display_size),dtype=np.float32)
        ax4=fig1.add_subplot(1,1,1)
        line_true_label, = ax4.plot(ydata_true_label,label='true_label')
        ax4.set_yticks(range(num_output))
        ax4.set_yticklabels(['{}'.format(config['label_set']['num2label'][str(j)]) for j in range(num_output)],rotation=30, fontsize='small')
        ax4.set_ylim([-0.1, num_output-1+0.1])
        ax4.legend(loc='lower left')

        def update_true_label():
            line_true_label.set_ydata(ydata_true_label)
            plt.draw()

    
    def update_line(j):
        line[j][0].set_ydata(ydata[:,j])
        plt.draw()
        return j
    
    def update_line_freq(j):
        line_freq[j][0].set_ydata(ydata_freq[:,j])
        plt.draw()
        return j

    if DEBUG:
        path = '/Users/futa/Documents/RESEARCH/sleep_eeg/database/sleep-edfx/SC4001E0-PSG.edf.mat'
        config['Fs'] = 100
        mat = loadmat(path)
        mat_signal = np.asarray(mat['signals'])[:,0]
        filtered_mat_signal = apply_filter(mat_signal,config['Fs'])
        mat_ann = np.asarray(mat['ann'])
        temp_label = 0
        temp_label_index = 0
        mat_comment = np.asarray(mat['comments'])
        mat_label = np.array([mat_comment[i][0][0].split(" ")[0] for i in range(mat_comment.shape[0])])
        matindex = 0
        list_predict =[]

    
    t_buflen = 0
    buf = []
    buff = None
    base_time = time.time()
    t_time = 0
    if PRED_NORM:
        pred_list = []

    while True:
        if DEBUG:
            if matindex + config['time_window'] > mat_signal.shape[0]:
                print('index exceed')
                break
            if matindex > mat_ann[temp_label_index+1]:
                temp_label = np.squeeze(mat_ann[temp_label_index+1])
                temp_label_index += 1
            # chunk = np.random.normal(size=(config['time_window']))
            chunk = mat_signal[matindex:matindex+config['time_window']]
            matindex += config['time_window']
            timestamps = 1
        else:
            chunk, timestamps = inlet.pull_chunk()

        if timestamps:
            if DEBUG:
                chunk, timestamps = np.asarray(chunk), np.asarray(timestamps)
            else:
                chunk, timestamps = np.asarray(chunk)[:,16]-np.asarray(chunk)[:,2], np.asarray(timestamps) # Fp1-Cz
            t_buflen += chunk.shape[0]
            buf.append(chunk)
            if t_buflen>=config['time_window']*int(config['Fs']/config['time_window']):
                con_tbuf = np.concatenate(buf,axis=0)

                if not DEBUG:
                    con_tbuf = con_tbuf*10e-2 # convert to micro


                if not buff is None:
                    buff = np.concatenate([buff,con_tbuf],axis=0)
                    if buff.size > 1000:
                        buff = buff[-1000:]
                else:
                    buff = con_tbuf

                ####
                #freq_chunk = con_buf[:config['time_window']*int(config['Fs']/config['time_window']),16] 
                # Fp1 ch17 Fp2 ch13 #ch7,8 are empty??
                
                #freq_chunk = scisig.decimate(freq_chunk,int(config['Fs']/config['time_window']),axis=0)
                #freq_chunk = apply_filter(freq_chunk,Fs=config['time_window'])
                #####

                # freq_chunk = scisig.decimate(buff,int(config['Fs']/config['time_window']),axis=0) if not DEBUG else buff

                # freq_chunk = scisig.decimate(buff,int(config['Fs']/config['time_window']),n=30,axis=0) if not DEBUG else scisig.resample(buff,int(buff.shape[0]*config['Fs']/config['time_window']),axis=0)
                if not DEBUG:
                    freq_chunk = apply_filter(buff,config['Fs'],'low')
                else:
                    # freq_chunk = apply_filter(buff,config['Fs'],'low',highcut=49.5)
                    freq_chunk = buff
                freq_chunk = apply_filter(freq_chunk,config['Fs'],'high')
                freq_chunk = scisig.resample(freq_chunk,int(buff.shape[0]*config['Fs']/config['time_window']),axis=0)
                freq_chunk = apply_filter(freq_chunk,Fs=config['time_window'])
                # if DEBUG and False:
                #     if freq_chunk.shape[0] < 2*config['time_window'] :
                #         freq_chunk = freq_chunk[-config['time_window']:,:]
                #     elif freq_chunk.shape[0] < 3*config['time_window'] :
                #         freq_chunk = freq_chunk[-config['time_window']*2:-config['time_window'],:]
                #     elif freq_chunk.shape[0] < 4*config['time_window'] :
                #         freq_chunk = freq_chunk[-config['time_window']*3:-config['time_window']*2,:]
                #     elif freq_chunk.shape[0] < 5*config['time_window'] :
                #         freq_chunk = freq_chunk[-config['time_window']*4:-config['time_window']*3,:]
                #     elif freq_chunk.shape[0] < 6*config['time_window'] :
                #         freq_chunk = freq_chunk[-config['time_window']*5:-config['time_window']*4,:]
                #     else:
                #         freq_chunk = freq_chunk[-config['time_window']*6:-config['time_window']*5,:]
                # else:
                freq_chunk = freq_chunk[-config['time_window']:,:]
                
                ydata_freq = np.concatenate((ydata_freq,freq_chunk),axis=0)[config['time_window']:]
                list(map(update_line_freq,range(len(line_freq))))

                # if DEBUG:
                #     freq_chunk = filtered_mat_signal[matindex:matindex+config['time_window']]

                freq_chunk = np.reshape(freq_chunk,(1,config['time_window'],config['input_len']))
                predict = net.model.predict(freq_chunk,batch_size=1)
                if PRED_NORM:
                    if len(pred_list)>=10:
                        pred_list.append(predict)
                        pred_list = pred_list[-10:]
                        predict = np.mean(np.asarray(pred_list),axis=0)
                    else:
                        pred_list.append(predict)

                if predict.shape == (1,num_output,num_output):
                    predict = predict[:,0,:]

                if DEBUG:
                    list_predict.append(predict)
                    ydata_true_label = np.concatenate((ydata_true_label,np.asarray([temp_label])),axis=0)[1:]
                    update_true_label()

                predict = np.reshape(predict,(1,num_output))

                #plt.ylim([ymin, ymax])
                ydata = np.concatenate((ydata,predict),axis=0)[1:]
                list(map(update_line,range(len(line))))

                circle.set_radius(sum(predict[0][1:]))
                plt.pause(pause_time)
                buf = [con_tbuf[config['time_window']*int(config['Fs']/config['time_window']):]]
                t_buflen = buf[0].shape[0]
                # print(t_buflen)
                t_time += config['time_window']/config['Fs']
                print('actual time: {}s'.format(time.time()-base_time),
                      'processed time: {}s'.format(t_time))

if DEBUG:
    np.savetxt('DEBUG_predict.csv',np.concatenate(np.asarray(list_predict),axis=0),delimiter=',')
KTF.set_session(old_session)


# In[ ]:


def test_load_and_predict():
    old_session = KTF.get_session()
    with tf.Graph().as_default():
        session = tf.Session('')
        KTF.set_session(session)
        net = Network(config)
        net.load('saved_models/20171212-084201')
        print(net.input_shape)
        predict = net.model.predict(np.zeros((1,100,5),dtype=np.float32),batch_size=1)
        print(predict)


# In[ ]:


def test_realtime_plot():
    from pylsl import StreamInlet, resolve_stream
    import numpy as np
    import scipy.signal as scisig
    import matplotlib.pyplot as plt
    import time

    figsize = (20,8)
    ymin, ymax = 0, 1
    max_display_size = 1000
    num_output= config['output_len']
    pause_time = 0.001


    plt.figure(figsize=figsize)
    plt.ion()

    ydata = np.zeros((max_display_size,num_output),dtype=np.float32)
    ax1=plt.axes()

    line = ax1.plot(ydata)
    plt.ylim([ymin, ymax])
    data = np.random.normal(size=(1,num_output))*0.1

    def update_line(j):
        line[j].set_ydata(ydata[:,j])
        plt.draw()
        return j

    while True:  
        d = np.random.normal(size=(1,num_output))*0.01
        data += d
        data = data/np.sum(data)
        print(data)
        plt.ylim([ymin, ymax])
        ydata = np.concatenate((ydata,data),axis=0)[1:]
        list(map(update_line,range(len(line))))
        plt.pause(pause_time)
    #     if i>100:
    #         break


# In[ ]:


def test_get_stream_and_data():
    # first resolve an EEG stream on the lab network
    i = 100
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    print("detect {} EEG streams!".format(len(streams)))
    inlet = StreamInlet(streams[0],max_buflen=360, max_chunklen=100, recover=True, processing_flags=0)
    while True:
        chunk, timestamps = inlet.pull_chunk()
        if timestamps:
            chunk, timestamps = np.asarray(chunk), np.asarray(timestamps)
            print('chunk shape: ',chunk.shape)
            i += 1
            if i>100: break

