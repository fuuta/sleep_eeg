
### 実行環境
- python 3.6.3

### 主要packageのversion (他は大体anacondaを使えばokです)
- tensorflow 1.4.0
- keras 2.1.2

学習済みモデルは[ここ](https://www.dropbox.com/s/9tw7mywsd8bl9c2/20171221-065527.zip?dl=0) からダウンロードして，shared/naruto下に展開してください．




### 実行手順
1. NICを立ち上げる．
2. 設定をloadする．(standard mount.txtをimportしてください)
3. NICで正しく脳波が取れていることを確認
4. 以下のコマンドを実行
``` bash
python sleep_eeg/AutoSleepScorer/sleepscorer/RUN_sleepscorer.py
```
5. 正常にEEG-PC間の通信ができている場合は，グラフが表示されます．
```looking for an EEG stream...```が出力されて，それ以上動かない場合はEG-PC間の通信に問題が有ります．

### 実際の出力例
```
/Users/futa/anaconda3/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: compiletime version 3.5 of module 'tensorflow.python.framework.fast_tensor_util' does not match runtime version 3.6
  return f(*args, **kwds)
Using TensorFlow backend.
2018-01-19 18:13:27.533275: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
create model
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv1d_1 (Conv1D)            (None, 34, 128)           32128     
_________________________________________________________________
batch_normalization_1 (Batch (None, 34, 128)           512       
_________________________________________________________________
dropout_1 (Dropout)          (None, 34, 128)           0         
_________________________________________________________________
conv1d_2 (Conv1D)            (None, 30, 256)           164096    
_________________________________________________________________
batch_normalization_2 (Batch (None, 30, 256)           1024      
_________________________________________________________________
dropout_2 (Dropout)          (None, 30, 256)           0         
_________________________________________________________________
max_pooling1d_1 (MaxPooling1 (None, 15, 256)           0         
_________________________________________________________________
conv1d_3 (Conv1D)            (None, 6, 300)            384300    
_________________________________________________________________
batch_normalization_3 (Batch (None, 6, 300)            1200      
_________________________________________________________________
dropout_3 (Dropout)          (None, 6, 300)            0         
_________________________________________________________________
max_pooling1d_2 (MaxPooling1 (None, 3, 300)            0         
_________________________________________________________________
conv1d_4 (Conv1D)            (None, 1, 512)            461312    
_________________________________________________________________
batch_normalization_4 (Batch (None, 1, 512)            2048      
_________________________________________________________________
dropout_4 (Dropout)          (None, 1, 512)            0         
_________________________________________________________________
dense_1 (Dense)              (None, 1, 1500)           769500    
_________________________________________________________________
batch_normalization_5 (Batch (None, 1, 1500)           6000      
_________________________________________________________________
dropout_5 (Dropout)          (None, 1, 1500)           0         
_________________________________________________________________
dense_2 (Dense)              (None, 1, 1500)           2251500   
_________________________________________________________________
batch_normalization_6 (Batch (None, 1, 1500)           6000      
_________________________________________________________________
dropout_6 (Dropout)          (None, 1, 1500)           0         
_________________________________________________________________
dense_3 (Dense)              (None, 1, 3)              4503      
_________________________________________________________________
activation_1 (Activation)    (None, 1, 3)              0         
=================================================================
Total params: 4,084,123
Trainable params: 4,075,731
Non-trainable params: 8,392
_________________________________________________________________
load existing params
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv1d_1 (Conv1D)            (None, 34, 128)           32128     
_________________________________________________________________
batch_normalization_1 (Batch (None, 34, 128)           512       
_________________________________________________________________
dropout_1 (Dropout)          (None, 34, 128)           0         
_________________________________________________________________
conv1d_2 (Conv1D)            (None, 30, 256)           164096    
_________________________________________________________________
batch_normalization_2 (Batch (None, 30, 256)           1024      
_________________________________________________________________
dropout_2 (Dropout)          (None, 30, 256)           0         
_________________________________________________________________
max_pooling1d_1 (MaxPooling1 (None, 15, 256)           0         
_________________________________________________________________
conv1d_3 (Conv1D)            (None, 6, 300)            384300    
_________________________________________________________________
batch_normalization_3 (Batch (None, 6, 300)            1200      
_________________________________________________________________
dropout_3 (Dropout)          (None, 6, 300)            0         
_________________________________________________________________
max_pooling1d_2 (MaxPooling1 (None, 3, 300)            0         
_________________________________________________________________
conv1d_4 (Conv1D)            (None, 1, 512)            461312    
_________________________________________________________________
batch_normalization_4 (Batch (None, 1, 512)            2048      
_________________________________________________________________
dropout_4 (Dropout)          (None, 1, 512)            0         
_________________________________________________________________
dense_1 (Dense)              (None, 1, 1500)           769500    
_________________________________________________________________
batch_normalization_5 (Batch (None, 1, 1500)           6000      
_________________________________________________________________
dropout_5 (Dropout)          (None, 1, 1500)           0         
_________________________________________________________________
dense_2 (Dense)              (None, 1, 1500)           2251500   
_________________________________________________________________
batch_normalization_6 (Batch (None, 1, 1500)           6000      
_________________________________________________________________
dropout_6 (Dropout)          (None, 1, 1500)           0         
_________________________________________________________________
dense_3 (Dense)              (None, 1, 3)              4503      
_________________________________________________________________
activation_1 (Activation)    (None, 1, 3)              0         
=================================================================
Total params: 4,084,123
Trainable params: 4,075,731
Non-trainable params: 8,392
_________________________________________________________________
looking for an EEG stream...

```


