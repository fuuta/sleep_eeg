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
        self.label2num = label_sets[0]['sets']
        self.num_label = label_sets[0]['num_label']
        # self.sd = sleeploader.SleepData(path)

    def define_labelset_and_time_window(self,label_set=0,time_window=500):
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

            self.EEG_Fpz_Cz = self.signals[:,0]
            self.EEG_Fpz_Cz = np.dstack([butter_bandpass_filter(self.EEG_Fpz_Cz, b[1][0], b[1][1], self.Fs, order=6)
                                         for b in freq_bands]).squeeze()

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
        assert self.EEG_Fpz_Cz.shape[0] == self.x.shape[0]