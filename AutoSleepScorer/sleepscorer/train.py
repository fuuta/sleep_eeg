from omazinai_for_debug import omazinai
omazinai()

import numpy as np
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

import keras.callbacks
import keras.backend.tensorflow_backend as KTF

from Network import Network
from json_encoder import JsonEncoder

pp = pprint.PrettyPrinter(indent=4)


os.chdir(os.path.dirname(os.path.abspath(__file__)))
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


old_session = KTF.get_session()

def create_dataset(config):
    file_name = os.path.join(home_path,'datasets',"tw_{}_ls_{}_il_{}_bs_{}".format(config['time_window'],config['label_set_index'],config['input_len'],config['batch_size']))
    Dt = [[],[]]
    repeated_y = 3 ## caution!!!!
    if os.path.exists(file_name):
        print('exists dir {}'.format(file_name))
        tfiles = glob.glob(os.path.join(file_name,'*.pkl'))
        print("length of Datasets: {}".format(len(tfiles)))
        for tfile in tfiles[:3]:
            print('load: ',tfile)
            with open(tfile,'rb') as f:
                (x_train, y_train, x_test, y_test) = cPickle.load(f)
            if config['input_len'] == 1:
                x_train = np.transpose(x_train, (0, 2, 1))
                x_test = np.transpose(x_test, (0, 2, 1))
            y_train = np.repeat(y_train, repeated_y,axis=1)
            y_test = np.repeat(y_test, repeated_y,axis=1)
            Dt[0].append(np.concatenate((x_train,x_test),axis=0))
            Dt[1].append(np.concatenate((y_train,y_test),axis=0))
    else:
        print('DD not found {}'.format(file_name))
        exit(1)

    x_train = np.concatenate(Dt[0],axis=0)
    y_train = np.concatenate(Dt[1],axis=0)
    ind = int(config['test_rate']*x_train.shape[0])
    x_test = x_train[-ind:]
    y_test = y_train[-ind:]
    x_train = x_train[:-ind]
    y_train = y_train[:-ind]
    print('x_train: {}'.format(x_train.shape))
    print('x_test: {}'.format(x_test.shape))
    print('y_train: {}'.format(y_train.shape))
    print('y_test: {}'.format(y_test.shape))

    return x_train, y_train, x_test, y_test

x_train, y_train, x_test, y_test = create_dataset(config)

with tf.Graph().as_default():
    session = tf.Session('')
    KTF.set_session(session)

    net = Network(config)

    tb_cb = keras.callbacks.TensorBoard(log_dir=net.log_dir, histogram_freq=1)
    cp_cb = keras.callbacks.ModelCheckpoint(filepath = os.path.join(net.save_dir,'cnn_model{epoch:02d}-loss{loss:.2f}-acc{acc:.2f}-vloss{val_loss:.2f}-vacc{val_acc:.2f}.hdf5'),
                                            monitor='val_loss', verbose=1, save_best_only=True, mode='auto')
    cbks = [tb_cb, cp_cb]

    history = net.model.fit(x_train, y_train, batch_size=config['batch_size'], epochs=config['n_epochs'], verbose=1, callbacks=cbks, validation_data=(x_test, y_test))
    score = net.model.evaluate(x_test, y_test, verbose=0)

    print('Test score:', score[0])
    print('Test accuracy:', score[1])

    net.save()
    print('save weights')

KTF.set_session(old_session)
