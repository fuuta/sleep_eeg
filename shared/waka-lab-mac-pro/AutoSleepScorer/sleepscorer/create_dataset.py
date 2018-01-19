import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import sleeploader
# import tools
import matplotlib
import time
import glob
import os,sys
import traceback
from scipy.io import loadmat
# import mne
import json
import pprint
from collections import Counter
import _pickle as cPickle
from multiprocessing import Pool

from scipy.signal import butter, lfilter
from scipy.signal import freqz
from keras.utils import np_utils


pp = pprint.PrettyPrinter(indent=4)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
home_path = os.getcwd()

config_list = json.load(open(os.path.join(home_path,'config_list.json'),'r'))
label_sets = config_list["label_sets"]
freq_bands = config_list["freq_bands"]


class Sleep_edfx(object):
    def __init__(self,path,time_window):
        self.path = path
        self.mat_path = path+'.mat'
        self.data_name = os.path.splitext(os.path.basename(self.mat_path))[0]

        self.time_window = time_window
        mat = loadmat(self.mat_path)
        self.signals = np.asarray(mat['signals'])
        self.Fs = np.asarray(mat['Fs'])
        self.tm = np.asarray(mat['tm'])

        self.ann = np.asarray(mat['ann'])
        self.anntype = mat['anntype']
        self.chan = mat['chan']
        self.comments = mat['comments']
        self.subtype = mat['subtype']
        self.num = mat['num']

        self.label = np.array([self.comments[i][0][0].split(" ")[0] for i in range(self.comments.shape[0])])
        self.label2num = label_sets['easy']['sets']
        self.num_label = label_sets['easy']['num_label']
        # self.sd = sleeploader.SleepData(path)

    def define_labelset_and_time_window(self,label_set='easy',time_window=500):
        def apply_filter():
            def butter_bandpass(lowcut, highcut, fs, order=5):
                nyq = 0.5 * fs
                low = lowcut / nyq
                high = highcut / nyq
                b, a = butter(order, [low, high], btype='bandpass')
                return b, a

            def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
                b, a = butter_bandpass(lowcut, highcut, fs, order=order)
                y = lfilter(b, a, data)
                return y

            self.EEG_Fpz_Cz = self.signals[:,0].squeeze()
            self.EEG_Fpz_Cz = np.dstack([butter_bandpass_filter(self.EEG_Fpz_Cz,
                                             freq_bands[b]['low'], 
                                             freq_bands[b]['high'], 100, order=6) for b in freq_bands]).squeeze()

        def change_time_window_size(time_window):
            # self.x = self.sd.get_data(epoch_len = time_window)
            if self.raw_y.shape[0]%time_window !=0 :
                self.raw_y = self.raw_y[:-(self.raw_y.shape[0]%time_window)]
            self.y = np.reshape(self.raw_y,(int(self.raw_y.shape[0]/time_window),time_window))
            df = pd.DataFrame(data=self.y)
            self.y = df.apply(lambda x: x.value_counts().idxmax(), axis=1)
            invert_dict =  {v: k for k, v in self.label2num.items()}
            counts = self.y.value_counts()
            self.count_y = [(invert_dict[i],counts[i]) for i in counts.keys()]

            # assert self.y.shape[0] == self.x.shape[0]

        self.label2num = label_sets[label_set]['sets']
        self.num_label = label_sets[label_set]['num_label']

        before_y = self.label2num['Sleep_stage_W']
        before_i = 0
        self.raw_y = []
        for tann,tlabel in zip(self.ann,self.label):
            self.raw_y += [before_y]*(tann[0]-before_i)
            before_i = tann[0]
            before_y = self.label2num[tlabel]
        self.raw_y += [before_y]*(self.tm.shape[0]-before_i)
        self.raw_y = np.asarray(self.raw_y)

        change_time_window_size(time_window)

        apply_filter()
        if self.EEG_Fpz_Cz.shape[0]%time_window !=0 :
            self.EEG_Fpz_Cz = self.EEG_Fpz_Cz[:-(self.raw_y.shape[0]%time_window),:,:]
            print(self.EEG_Fpz_Cz.shape)

        self.EEG_Fpz_Cz = np.reshape(self.EEG_Fpz_Cz,
                                     (int(self.EEG_Fpz_Cz.shape[0]/time_window),time_window,self.EEG_Fpz_Cz.shape[-1]))
        # assert self.EEG_Fpz_Cz.shape[0] == self.x.shape[0]


def wrapper(args):
    create_dataset(*args)

def create_dataset(t,time_window,label_set,n_output,batch_size):
    try:
        print(t)
        temp_dat = Sleep_edfx(t,time_window)
        temp_dat.define_labelset_and_time_window(label_set=label_set,time_window=time_window)
        #         Datas[-1].change_time_window_size(time_window)

        def split_data(x, y, ratio: int = 0.9):
            to_train = int(int(x.shape[0]*ratio)/batch_size)*batch_size
            trash = x.shape[0]%batch_size
            print ('To train datas:',to_train,' Trash:' , trash)

            #             x = np.reshape(x,(int(x.size/(input_len*n_input)),input_len,n_input))
            y = np_utils.to_categorical(y,num_classes=n_output)
            y = np.reshape(y,(int(y.size/(n_output)),1,n_output))
            x_train = x[:to_train]
            y_train = y[:to_train]
            x_test = x[to_train:-trash]
            y_test = y[to_train:-trash]

            return (x_train, y_train), (x_test, y_test)

        #         data_input = temp_dat.x[:,:,0]
        data_input = temp_dat.EEG_Fpz_Cz
        expected_output = temp_dat.y
        print(data_input.shape,expected_output.shape)
        print(temp_dat.count_y)

        # shuffle data
        shuffle_indexes = np.asarray(range(data_input.shape[0]))
        np.random.shuffle(shuffle_indexes)
        shuffled_data_input = data_input[shuffle_indexes]
        shuffled_expected_output = expected_output[shuffle_indexes]

        (x_train, y_train), (x_test, y_test) = split_data(shuffled_data_input, shuffled_expected_output)
        print('x_train.shape: ', x_train.shape)
        print('y_train.shape: ', y_train.shape)
        print('x_test.shape: ', x_test.shape)
        print('y_test.shape: ', y_test.shape)

        print("Done! load {}".format(t))
        final_path = os.path.join(save_dataset_path,os.path.splitext(os.path.basename(t))[0])+'.pkl'
        with open(final_path,'wb') as f:
            cPickle.dump((x_train, y_train, x_test, y_test), f)
        print('pickle dump {}\n\n'.format(final_path))
    except Exception:
        exc_info = sys.exc_info()
        # Display the *original* exception
        traceback.print_exception(*exc_info)
        del exc_info

home = '/home/f-tomita/share/sleep_eeg'
dataset_dir = os.path.join(home,'AutoSleepScorer','sleepscorer','datasets')

dataset_path = os.path.join(home,'database','sleep-edfx')
dirs = glob.glob(os.path.join(dataset_path,'*.edf'))

# config
time_window = 100
label_set = 'easy'
n_input = time_window
input_len = len(freq_bands)
batch_size = 128
n_output = label_sets[label_set]['num_label']
#


d_path = "tw_{}_ls_{}_il_{}_bs_{}".format(time_window,label_set,input_len,batch_size)
save_dataset_path = os.path.join(dataset_dir, d_path)

if not os.path.exists(save_dataset_path):
    os.mkdir(save_dataset_path)
print (save_dataset_path)


with Pool(12) as p:
    argss=[(d,time_window,label_set,n_output,batch_size) for d in dirs]
    p.map(wrapper, argss)
print('All Done!!')