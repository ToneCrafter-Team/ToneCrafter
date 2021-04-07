import pyaudio
import numpy as np
import ddsp
import ddsp.training
from ddsp.colab.colab_utils import (specplot, DEFAULT_SAMPLE_RATE)
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
import sounddevice as sd


FORMAT = pyaudio.paFloat32
RATE = 16000
CHUNK = 2048
RECORD_SECONDS = 60
CHANNELS = 2

p =   pyaudio.PyAudio()

player = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, 
frames_per_buffer=CHUNK)
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)


##Création d'une fonction de distortion
def distortion(A,audio):
    k = 2*A/(1-A)
    audio_out = (1+k)*abs(audio)/(1+k*audio)
    return audio_out


##Ecoute en temps réel des hauts-parleurs 
for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
    a = np.fromstring(stream.read(CHUNK),dtype=np.float32)
    player.write(distortion(0.2,a),CHUNK)


stream.stop_stream()
stream.close()
p.terminate()
