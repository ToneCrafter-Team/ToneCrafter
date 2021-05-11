
import numpy as np

import matplotlib.pyplot as plt

import librosa
import librosa.display

from scipy import signal
from pitchdetector import pitchdetection
from pitchdetector import fichier

import soundfile as sf

from filtres import filtre_passe_bas
from filtres import filtre_passe_haut
from filtres import filtre_butter_passe_bas
from filtres import filtre_butter_passe_haut
from disto import disto
from timeeffect import reverb
from timeeffect import tremolo
from overdrive import overdrive_1
from overdrive import overdrive_2
from chorus import chorus
from chorus import flanger
from correlation import corrélation
from pitchdetector import pitchdetection
from bruitrose import pink_noise



x, sr = librosa.load('Moi.wav',offset=0.5, duration=5)
y=x
fs = sr  # Sample frequency (Hz)
length = 5  # seconds
f_sample = sr  # Hz

f_ref = 3000  # Hz, The frequency for max amplitude

f_min = 10  # Hz
f_max = 20000  # hz



sig = pink_noise(f_ref, f_min, f_max, length, f_sample)
y=x+0.001*sig
y=disto(y,800)
y=tremolo(y,6,0.2,fs)
fc =  6600
y=filtre_butter_passe_bas(y,fc,fs)
fc = 1060
y=filtre_passe_haut(y,fc)
y=chorus(y,50,50,50,0.15,0.2,0.3,10,0.25,0.25,0.25,fs)
y=reverb(y,0.2,fs)
y = 0.8 * y / max(abs(y))
sf.write('0-Moi_disto.wav', y, sr)




sig = pink_noise(f_ref, f_min, f_max, length, f_sample)
y=x+0.001*sig
y=overdrive_1(y,97,15.9,15.6,0)
y=tremolo(y,6,0.2,fs)
fc =  6600
y=filtre_butter_passe_bas(y,fc,fs)
fc = 1060
y=filtre_passe_haut(y,fc)
y=chorus(y,50,50,50,0.15,0.2,0.3,10,0.25,0.25,0.25,fs)
y=reverb(y,0.2,fs)
y = 0.8 * y / max(abs(y))
sf.write('0-Moi_overdrive1.wav', y, sr)



sig = pink_noise(f_ref, f_min, f_max, length, f_sample)
y=x+0.001*sig
y=overdrive_2(y,600,0)
y=tremolo(y,6,0.2,fs)
fc =  6600
y=filtre_butter_passe_bas(y,fc,fs)
fc = 1060
y=filtre_passe_haut(y,fc)
y=chorus(y,50,50,50,0.15,0.2,0.3,10,0.25,0.25,0.25,fs)
y=reverb(y,0.2,fs)
y = 0.8 * y / max(abs(y))
sf.write('0-Moi_overdrive2.wav', y, sr)
