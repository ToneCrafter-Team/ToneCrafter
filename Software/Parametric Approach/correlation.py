# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:01:48 2021

@author: duwat
"""
import numpy as np
import librosa
import librosa.display




ro=2**14
n_fft=ro
hop_length = 256


x, sr = librosa.load('G53-40100-1111-00001.wav',offset=0)
y, sr = librosa.load('G53-41101-1111-00002.wav',offset=0)

D = librosa.amplitude_to_db(np.abs(librosa.stft(x, n_fft =ro,hop_length=hop_length)), ref=np.max)
D1=D.tolist()

D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft =ro,hop_length=hop_length)), ref=np.max)
D2=D.tolist()

def corrélation(x,y):
    
    D1 = librosa.amplitude_to_db(np.abs(librosa.stft(x, n_fft =ro,hop_length=hop_length)), ref=np.max)
    D2 = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft =ro,hop_length=hop_length)), ref=np.max)
    X=D1.tolist()
    Y=D2.tolist()
    a=0
    for i in range(len(X)):
        for j in range (len(X[i])):
            x1=X[i][j]
            x2=Y[i][j]
            a=a+((x1-x2)**2)
    o=a/(len(X)*len(Y))
    return o
        