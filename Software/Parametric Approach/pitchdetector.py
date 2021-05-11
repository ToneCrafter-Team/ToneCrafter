# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:04:28 2021

@author: duwat
"""


import numpy as np
import librosa
import librosa.display

from scipy import signal



output_file = 'G53-41101-1111-00002.wav'

x, sr = librosa.load('G53-41101-1111-0000'+str(2)+".wav",offset=0)
y=x


    
fs = sr  # Sample frequency (Hz)

Notestriees=[[32.70,  65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01,  8372.02 ],
             [34.65,  69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92,  8869.84 ],
             [36.71,  73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64,  9397.28 ],
             [38.89,  77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03,  9956.06 ],
             [41.20,  82.41, 164.81, 329.63, 659.26, 1318.51, 2637.02, 5274.04, 10548.08 ],
             [43.65,  87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65, 11175.30 ],
             [46.25,  92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91, 11839.82 ],
             [49.00,  98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93, 12543.86 ],
             [51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88, 13289.76 ],
             [55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00, 14080.00 ],
             [58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62, 14917.24 ],
             [61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13, 15804.26 ]]


Notes=[32.70,  65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01,  8372.02 ,
       34.65,  69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92,  8869.84 ,
       36.71,  73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64,  9397.28 ,
       38.89,  77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03,  9956.06 ,
       41.20,  82.41, 164.81, 329.63, 659.26, 1318.51, 2637.02, 5274.04, 10548.08 ,
       43.65,  87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65, 11175.30 ,
       46.25,  92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91, 11839.82 ,
       49.00,  98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93, 12543.86 ,
       51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88, 13289.76 ,
       55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00, 14080.00 ,
       58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62, 14917.24 ,
       61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13, 15804.26 ]


Notesecritestrans=["Do0","Do#0", "Ré0", "Ré#0", "Mi0", "Fa0", "Fa#0", "Sol#0", "La0", "La#0", "Si0",
              "Do1","Do#1", "Ré1", "Ré#1", "Mi1", "Fa1", "Fa#1", "Sol#1", "La1", "La#1", "Si1",
              "Do2","Do#2", "Ré2", "Ré#2", "Mi2", "Fa2", "Fa#2", "Sol#2", "La2", "La#2", "Si2",
              "Do3","Do#3", "Ré3", "Ré#3", "Mi3", "Fa3", "Fa#3", "Sol#3", "La3", "La#3", "Si3",
              "Do4","Do#4", "Ré4", "Ré#4", "Mi4", "Fa4", "Fa#4", "Sol#4", "La4", "La#4", "Si4",
              "Do5","Do#5", "Ré5", "Ré#5", "Mi5", "Fa5", "Fa#5", "Sol#5", "La5", "La#5", "Si5",
              "Do6","Do#6", "Ré6", "Ré#6", "Mi6", "Fa6", "Fa#6", "Sol6#", "La6", "La#6", "Si6",
              "Do7","Do#7", "Ré7", "Ré#7", "Mi7", "Fa7", "Fa#7", "Sol#7", "La7", "La#7", "Si7",
              "Do8","Do#8", "Ré8", "Ré#8", "Mi8", "Fa8", "Fa#8", "Sol#8", "La8", "La#8", "Si8"]
              
Notesecrites=np.transpose(Notesecritestrans)

Note=[]
for i in range(9):
    for j in range(12):
        Note.append(Notestriees[j][i])

L=[]
for i in range (len(Notes)-1):
    a=np.sqrt(Note[i]*Note[i+1])
    L.append(a)
   
    
    
##Filtrage 
ro=2**14
Q = 5  # Quality factor
n_fft=ro


for i in range(len(L)):
    
    b, a = signal.iirnotch(L[i]*2/fs, Q, fs)
    zi =signal.lfilter_zi(b, a)
    z = signal.filtfilt(b, a, x)
    x=z
    
def pitchdetection(x):
    ro=2**14
        
    hop_length = 256
    
    
    D = librosa.amplitude_to_db(np.abs(librosa.stft(x, n_fft =ro,hop_length=hop_length)), ref=np.max)
    M=D.tolist()
    
    K=[]
    for i in range(int(len(M)/2)):
        K.append(2*i*fs/ro)
    Mean=[]
    M2=[]
    
    for i in range (len(M)-24):
        M2.append(M[i+23])
    
    for i in range (len(M2)):
        Mean.append(np.mean(M2[i]))
        
    a=np.max(Mean)
    Meanrangée=sorted(Mean)
    
    Freq=[]
    
    
    n= len(Meanrangée)
    for i in range (10):
        b=Mean.index(Meanrangée[n-i-1])
        Freq.append(((b+24)*fs/ro))
        
    FreqNorm=[]
    
    
    
    for i in range (len(Freq)):
        a=Freq[i]
        j=0
        b=Note[j]
        c=Note[j+1]
        while a>np.sqrt(b*c):
            j=j+1
            b=Note[j]
            c=Note[j+1]
            
        c=Note[j]
        FreqNorm.append(c)
    
    
    a=min(FreqNorm)
    b=Note.index(a)
    return [Notesecrites[b],b-35]
    
def fichier(n):
    
    Liste=[]
    if n<6:
        Liste.append("G53-"+str(40+n)+str(100+n   ).zfill(3)+"-1111-"+str(n+1   ).zfill(5))
    elif n<11:
        Liste.append("G53-"+str(40+n)+str(100+n   ).zfill(3)+"-1111-"+str(n+1   ).zfill(5))
        Liste.append("G53-"+str(40+n)+str(200+n-5 ).zfill(3)+"-1111-"+str(n+1+8 ).zfill(5))
    elif n<13:
        Liste.append("G53-"+str(40+n)+str(100+n   ).zfill(3)+"-1111-"+str(n+1   ).zfill(5))
        Liste.append("G53-"+str(40+n)+str(200+n-5 ).zfill(3)+"-1111-"+str(n+1+8 ).zfill(5))
        Liste.append("G53-"+str(40+n)+str(300+n-10).zfill(3)+"-1111-"+str(n+1+16).zfill(5))
    elif n<16:
        Liste.append("G53-"+str(40+n)+str(200+n-5 ).zfill(3)+"-1111-"+str(n+1+8 ).zfill(5))
        Liste.append("G53-"+str(40+n)+str(300+n-10).zfill(3)+"-1111-"+str(n+1+16).zfill(5))
    elif n<18:
        Liste.append("G53-"+str(40+n)+str(200+n-5 ).zfill(3)+"-1111-"+str(n+1+8 ).zfill(5))
        Liste.append("G53-"+str(40+n)+str(300+n-10).zfill(3)+"-1111-"+str(n+1+16).zfill(5))
        Liste.append("G53-"+str(40+n)+str(400+n-15).zfill(3)+"-1111-"+str(n+1+24).zfill(5))
    elif n<20:
        Liste.append("G53-"+str(40+n)+str(300+n-10).zfill(3)+"-1111-"+str(n+1+16).zfill(5))
        Liste.append("G53-"+str(40+n)+str(400+n-15).zfill(3)+"-1111-"+str(n+1+24).zfill(5))
    elif n<22: 
        Liste.append("G53-"+str(40+n)+str(300+n-10).zfill(3)+"-1111-"+str(n+1+16).zfill(5))
        Liste.append("G53-"+str(40+n)+str(400+n-15).zfill(3)+"-1111-"+str(n+1+24).zfill(5))
        Liste.append("G53-"+str(40+n)+str(500+n-19).zfill(3)+"-1111-"+str(n+1+33).zfill(5))
    elif n<25:
        Liste.append("G53-"+str(40+n)+str(400+n-15).zfill(3)+"-1111-"+str(n+1+24).zfill(5))
        Liste.append("G53-"+str(40+n)+str(500+n-19).zfill(3)+"-1111-"+str(n+1+33).zfill(5))
    elif n<27:
        Liste.append("G53-"+str(40+n)+str(400+n-15).zfill(3)+"-1111-"+str(n+1+24).zfill(5))
        Liste.append("G53-"+str(40+n)+str(500+n-19).zfill(3)+"-1111-"+str(n+1+33).zfill(5))
        Liste.append("G53-"+str(40+n)+str(600+n-24).zfill(3)+"-1111-"+str(n+1+41).zfill(5))
        
    return Liste