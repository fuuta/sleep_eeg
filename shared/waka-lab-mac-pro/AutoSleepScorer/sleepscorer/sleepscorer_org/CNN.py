
import numpy as np
import pandas as pd
import sleeploader
from sleepscorer_org import tools
import time
import glob
import os,sys
import traceback
import json
from scipy.io import loadmat
import mne
import pprint
from collections import Counter
import _pickle as cPickle
import time

import tensorflow as tf
from keras.backend import tensorflow_backend
config = tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))
session = tf.Session(config=config)
tensorflow_backend.set_session(session)

import keras
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Conv1D, MaxPooling1D
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential
from keras.utils import np_utils

pp = pprint.PrettyPrinter(indent=4)

label_sets = [
    {'sets':{'Sleep_stage_W':0,
                          'Sleep_stage_R':1,
                          'Sleep_stage_1':2,
                          'Sleep_stage_2':3,
                          'Sleep_stage_3':4,
                          'Sleep_stage_4':5,
                          'Sleep_stage_?':6,
                          'Movement_time':7,
                         },
    'num_label':8},
    {'sets':{'Sleep_stage_W':0,
                          'Sleep_stage_R':1,
                          'Sleep_stage_1':2,
                          'Sleep_stage_2':2,
                          'Sleep_stage_3':2,
                          'Sleep_stage_4':2,
                          'Sleep_stage_?':0,
                          'Movement_time':0,
                         },
    'num_label':3},
]


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'keras_CNN_trained_model.h5'

config = {}
config['time_window'] = 100
config['label_set_index']=  1
# config['label_set_index']=  0
config['label_set']= label_sets[config['label_set_index']]
config['batch_size']= 128
config['n_epochs']= 20
config['input_len']=5

print('load exists model?? ')
var = input()
if var == 'yes':
    print('input model path: ')
    model_path = input()
    assert os.path.isfile(model_path)
else:
    print('create new model')

timestr = time.strftime("%Y%m%d-%H%M%S")
save_dir = os.path.join(save_dir,timestr)
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
if not os.path.exists(os.path.join(save_dir,'memo.txt')):
    with open(os.path.join(save_dir,'memo.txt'), 'w') as f_memo:
        f_memo.write(" ")
if not os.path.exists(os.path.join(save_dir,'conf.json')):
    with open(os.path.join(save_dir,'conf.json'), 'w') as f_json:
        f_json.write(json.dumps(config,indent=4,sort_keys=True,cls=MyEncoder))

time_window =config['time_window'] 
input_len = config['input_len']
label_set = config['label_set_index']
batch_size = config['batch_size'] 
n_output = config['label_set']['num_label']
epochs = config['n_epochs']

file_name = "tw_{}_ls_{}_il_{}_bs_{}".format(time_window,label_set,input_len,batch_size)
Dt = [[],[]]

repeated_y = 3 ## caution!!!!

if os.path.exists(file_name):
    print('exists dir {}'.format(file_name))
    tfiles = glob.glob(os.path.join(file_name,'*.pkl'))
    print("length of Datasets: {}".format(len(tfiles)))
    for tfile in tfiles: 
        print('load: ',tfile)
        with open(tfile,'rb') as f:
            (x_train, y_train, x_test, y_test) = cPickle.load(f)
        if input_len == 1:
            x_train = np.transpose(x_train, (0, 2, 1))
            x_test = np.transpose(x_test, (0, 2, 1))
        y_train = np.repeat(y_train, repeated_y,axis=1)
        y_test = np.repeat(y_test, repeated_y,axis=1)
        Dt[0].append(np.concatenate((x_train,x_test),axis=0))
        Dt[1].append(np.concatenate((y_train,y_test),axis=0))
else: 
    print('DD not found')
    exit(1)



test_rate = 0.1
x_train = np.concatenate(Dt[0],axis=0)
y_train = np.concatenate(Dt[1],axis=0)
ind = int(test_rate*x_train.shape[0])
x_test = x_train[-ind:]
y_test = y_train[-ind:]
x_train = x_train[:-ind]
y_train = y_train[:-ind]
print('x_train: {}'.format(x_train.shape))
print('x_test: {}'.format(x_test.shape))
print('y_train: {}'.format(y_train.shape))
print('y_test: {}'.format(y_test.shape))


# In[ ]:


def model_1():
    model = Sequential()
    model.add(Conv1D(128, 50, strides=5, activation='relu',input_shape=(time_window,1)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Conv1D(256, 5, strides=1, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    
    model.add(MaxPooling1D(2))
    
    model.add(Conv1D(300, 5, strides=2,  activation='relu'))
    
    model.add(MaxPooling1D(2))
    
    model.add(Dense(1500))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(1500))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))    
    model.add(Dense(n_output))
    model.add(Activation('softmax'))
    return model

def model_for_100():
    model = Sequential()
    model.add(Conv1D(128, 50, strides=3, padding='same',activation='relu',input_shape=(time_window,input_len)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Conv1D(256, 5, strides=1, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    
    model.add(MaxPooling1D(2))
    
    model.add(Conv1D(300, 5, strides=2,  activation='relu'))
    
    model.add(MaxPooling1D(2))
    
    model.add(Dense(1500))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(1500))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))    
    model.add(Dense(n_output))
    model.add(Activation('softmax'))
    return model

def model_2(): # for image classification
    model = Sequential()
    model.add(Conv1D(128, (3, 3), padding='same',
                     input_shape=x_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))
    return model

#model = model_1()
model = model_for_100()
print(model.summary())


# In[ ]:


# initiate RMSprop optimizer
opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

# Let's train the model using RMSprop
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test),
          shuffle=True)

# Save model and weights
model_path = os.path.join(save_dir, model_name)

model.save(model_path)
print('Saved trained model at %s ' % model_path)

# Score trained model.
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

