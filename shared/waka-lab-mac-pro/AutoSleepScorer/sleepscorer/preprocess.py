
# coding: utf-8

# In[2]:


import numpy as np
import os,sys
import json
from scipy.signal import butter, lfilter
from scipy.signal import freqz

os.chdir(os.path.dirname(os.path.abspath(__file__)))
home_path = os.getcwd()

config_list = json.load(open(os.path.join(home_path,'config_list.json'),'r'))
label_sets = config_list["label_sets"]
freq_bands = config_list["freq_bands"]

def apply_filter(signal):
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
    return np.dstack([butter_bandpass_filter(np.random.normal(size=100), 
                                             freq_bands[b]['low'], 
                                             freq_bands[b]['high'], 100, order=6) for b in freq_bands]).squeeze()

