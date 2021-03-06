

import json
import os
import time
import numpy as np
import tensorflow as tf
from keras.backend import tensorflow_backend
from sklearn import metrics
import matplotlib as mpl
# mpl.use('Agg')
import matplotlib.pyplot as plt
import itertools

config = tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))
session = tf.Session(config=config)
tensorflow_backend.set_session(session)

import keras
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Conv1D, MaxPooling1D
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential
from json_encoder import JsonEncoder




class Network(object):
    def __init__(self,config):
        self.config = config
        self.input_shape = config['input_shape']
        self.output_len = config['output_len']
        self.model_type = config['model_type']
        self.model = self.model(config['model_type'])
        self.save_dir = os.path.join(config['home_path'], 'saved_models', time.strftime("%Y%m%d-%H%M%S"))
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        self.log_dir = os.path.join(self.save_dir,'logs')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        if not os.path.exists(os.path.join(self.save_dir,'memo.txt')):
            with open(os.path.join(self.save_dir,'memo.txt'), 'w') as f_memo:
                f_memo.write(" ")
        if not os.path.exists(os.path.join(self.save_dir,'conf.json')):
            with open(os.path.join(self.save_dir,'conf.json'), 'w') as f_json:
                f_json.write(json.dumps(config,indent=4,sort_keys=True,cls=JsonEncoder))

        open(os.path.join(self.save_dir,'cnn_model.json'), 'w').write(self.model.to_json())


    def model(self,model_type):
        print('create model')
        def model_1():
            model = Sequential()
            model.add(Conv1D(128, 50, strides=5, activation='relu',input_shape=self.input_shape))
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
            model.add(Dense(self.output_len))
            model.add(Activation('softmax'))
            return model

        def model_for_100():
            model = Sequential()
            model.add(Conv1D(128, 50, strides=3, padding='same',activation='relu',input_shape=self.input_shape))
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
            model.add(Dense(self.output_len))
            model.add(Activation('softmax'))
            return model

        def model_for_100_2():
            model = Sequential()
            model.add(Conv1D(128, 50, strides=3, padding='same',activation='relu',input_shape=self.input_shape))
            model.add(BatchNormalization())
            model.add(Dropout(0.2))
            model.add(Conv1D(256, 5, strides=1, activation='relu'))
            model.add(BatchNormalization())
            model.add(Dropout(0.2))

            model.add(MaxPooling1D(2))

            model.add(Conv1D(300, 5, strides=2,  activation='relu'))
            model.add(BatchNormalization())
            model.add(Dropout(0.2))

            model.add(MaxPooling1D(2))

            model.add(Conv1D(512, 3, strides=1, activation='relu'))
            model.add(BatchNormalization())
            model.add(Dropout(0.2))

            model.add(Dense(1500))
            model.add(BatchNormalization())
            model.add(Dropout(0.5))
            model.add(Dense(1500))
            model.add(BatchNormalization())
            model.add(Dropout(0.5))
            model.add(Dense(self.output_len))
            model.add(Activation('softmax'))
            return model

        def model_2(): # for image classification
            model = Sequential()
            model.add(Conv1D(128, (3, 3), padding='same',
                             input_shape=self.input_shape))
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
            model.add(Dense(self.output_len))
            model.add(Activation('softmax'))
            return model

        if model_type == 'LSTM':
            m = model_2()
        elif model_type == 'CNN':
            m =  model_for_100()
        elif model_type == 'CNN2':
            m =  model_for_100_2()
        elif model_type == 'CNN2LSTM':
            m =  model_1()
        else:
            raise Exception('model type not found')
        self.define_loss(m)
        return m

    def load(self,path):
        print('load existing params')
        if self.config['load'] == 'whole':
            if os.path.join(path,'model.json'):
                json_string = open(os.path.join(path,'cnn_model.json')).read()
                self.model = keras.models.model_from_json(json_string)
                self.model.load_weights(os.path.join(path,'Final_params.hdf5'))
                self.define_loss(self.model)
            else:
                raise Exception('model.json not found')
        elif self.config['load'] == 'partial':
            raise Exception('loading partially is not implement')

    def define_loss(self,model):
        model.summary()
        model.compile(loss=self.config['loss'],
                           optimizer=keras.optimizers.Adam(lr=0.001, beta_1=0.5),
                           metrics=['accuracy'])

    def pred(self,feeddict):
        print('prediction')

    def save(self,file_name = 'Final_params.hdf5'):
        self.model.save_weights(os.path.join(self.save_dir,file_name))

    def dump_confusion_matrix(self,x_test,y_test,batch_size):
        def plot_confusion_matrix(cm, classes,
                                  title='Confusion matrix',
                                  cmap=plt.cm.Blues):
            """
            This function prints and plots the confusion matrix.
            Normalization can be applied by setting `normalize=True`.
            """
            for normalize in [True,False]:
                plt.figure()
                if normalize:
                    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
                    print("Normalized confusion matrix")
                else:
                    print('Confusion matrix, without normalization')

                print(cm)

                plt.imshow(cm, interpolation='nearest', cmap=cmap)
                plt.title(title)
                plt.colorbar()
                tick_marks = np.arange(len(classes))
                plt.xticks(tick_marks, classes, rotation=45)
                plt.yticks(tick_marks, classes)

                fmt = '.2f' # if normalize else 'd'
                thresh = cm.max() / 2.
                for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
                    plt.text(j, i, format(cm[i, j], fmt),
                             horizontalalignment="center",
                             color="white" if cm[i, j] > thresh else "black")

                plt.tight_layout()
                plt.ylabel('True label')
                plt.xlabel('Predicted label')
                if normalize:
                    plt.savefig(os.path.join(self.save_dir,'Confusion_matrix_normalized.png'))
                else:
                    plt.savefig(os.path.join(self.save_dir,'Confusion_matrix.png'))

        pred = self.model.predict_classes(x_test,batch_size=batch_size)
        # confusion_matrix = tf.confusion_matrix(np.argmax(y_test[:,0,:],axis=-1),pred[:,0],num_classes=config['output_len'])
        confusion_matrix = metrics.confusion_matrix(y_true=np.argmax(y_test[:,0,:],axis=-1),y_pred=pred[:,0])
        for i in range(pred.shape[-1])[1:]:
            confusion_matrix += metrics.confusion_matrix(y_true=np.argmax(y_test[:,i,:],axis=-1),y_pred=pred[:,i])
        plot_confusion_matrix(confusion_matrix,['wake','rem','nonrem'])


