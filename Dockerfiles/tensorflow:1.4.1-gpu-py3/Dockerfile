FROM tensorflow/tensorflow:1.4.1-gpu-py3
MAINTAINER f-tomita <fuuta1995@gmail.com>
RUN echo 'now building image ...'
RUN apt-get update && apt-get install -y tk-dev python3-tk
RUN rm -rf /var/lib/apt/lists/*
RUN pip install mne keras seaborn

CMD echo  'now loading image ...'
WORKDIR /

