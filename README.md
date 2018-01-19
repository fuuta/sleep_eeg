全てDockerに移行しました．

matlabなどのコードはanotherに入ってます．

実行環境
- python 3.6.3

主要package (他は大体anacondaを使えばokです)
- tensorflow 1.4.0
- keras 2.1.2

学習済みモデルはここ(https://www.dropbox.com/s/9tw7mywsd8bl9c2/20171221-065527.zip?dl=0)からダウンロードして，shared/naruto下に展開してください．

実行command
python sleep_eeg/AutoSleepScorer/sleepscorer/RUN_sleepscorer.py