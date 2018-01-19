
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

def butter_highpass(lowcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = butter(order, low, btype='high')
    return b, a

def butter_highpass_filter(data, lowcut, fs, order=5):
    b, a = butter_highpass(lowcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lowpass(highcut, fs, order=5):
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = butter(order, high, btype='low')
    return b, a

def butter_lowpass_filter(data, highcut, fs, order=5):
    b, a = butter_lowpass( highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y



def apply_filter(signal,Fs=100,type='band',highcut=100,lowcut=1):
    if type == 'band':
        return np.dstack([butter_bandpass_filter(signal.squeeze(),
                                             freq_bands[b]['low'], 
                                             freq_bands[b]['high'], Fs, order=6) for b in freq_bands]).squeeze()
    elif type == 'high':
        return butter_highpass_filter(signal.squeeze(),lowcut,Fs,order=6)
    elif type == 'low':
        return butter_lowpass_filter(signal.squeeze(),highcut,Fs,order=6)

