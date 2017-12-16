
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

import pandas as pd
import glob
import os
import json
import pprint
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

config['model_type']='CNN'
config['time_window'] = 100
config['input_len']=5
config['output_len']= config['label_set']['num_label']
config['input_shape']=(config['time_window'],config['input_len'])

config['batch_size']= 128
config['loss']= 'categorical_crossentropy'
config['n_epochs']= 4
config['test_rate']=0.1


# In[ ]:


config['load']='whole'

figsize = (20,8)
ymin, ymax = 0, 1
max_display_size = 1000
num_output= config['output_len']
pause_time = 0.001
DEBUG=True

old_session = KTF.get_session()
with tf.Graph().as_default():
    session = tf.Session('')
    KTF.set_session(session)
    net = Network(config)
    net.load('saved_models/20171212-084201')

    if not DEBUG:
        print("looking for an EEG stream...")
        streams = resolve_stream('type', 'EEG')
        print("detect {} EEG streams!".format(len(streams)))
        inlet = StreamInlet(streams[0],max_buflen=360, max_chunklen=100, recover=True, processing_flags=0)
    
    fig = plt.figure(figsize=figsize)
    plt.ion()

    ydata = np.zeros((max_display_size,num_output),dtype=np.float32)
    ax1=fig.add_subplot(2,1,1)
    line = [ax1.plot(ydata[:,j],label='output {}'.format(j)) for j in range(num_output)]
    ax1.set_ylim([ymin, ymax])
    
    ax2=fig.add_subplot(2,1,2)
    ax2.set_aspect('equal')
    circle = Circle((0, 0), 1)
    ax2.add_artist(circle)
    ax2.set_xlim([-1, 1])
    ax2.set_ylim([-1, 1])
    
    plt.legend()
    def update_line(j):
        line[j][0].set_ydata(ydata[:,j])
        plt.draw()
        return j
    
    while True:
        if not DEBUG:
            chunk, timestamps = inlet.pull_chunk()
        else:
            chunk = np.random.normal(size=(config['time_window']))
            timestamps = 'hogehoge'
        
        if timestamps:
            chunk, timestamps = np.asarray(chunk), np.asarray(timestamps)
            print('chunk shape: ',chunk.shape)
            assert chunk.size == 100
            freq_chunk = apply_filter(chunk)
            freq_chunk = np.reshape(freq_chunk,(1,config['time_window'],config['input_len']))
            predict = net.model.predict(freq_chunk,batch_size=1)
            if predict.shape == (1,num_output,num_output):
                predict = predict[:,0,:]
            print(predict)
            predict = np.reshape(predict,(1,num_output))
            #plt.ylim([ymin, ymax])
            ydata = np.concatenate((ydata,predict),axis=0)[1:]
            list(map(update_line,range(len(line))))
            circle.set_radius(sum(predict[0][1:]))
            plt.pause(pause_time)
    
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

