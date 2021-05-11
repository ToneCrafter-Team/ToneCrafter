import pyaudio
import numpy as np

from filtres import filtre_passe_bas
from filtres import filtre_passe_haut
from filtres import filtre_butter_passe_bas
from filtres import filtre_butter_passe_haut
from disto import disto
from timeeffect import reverb
from overdrive import overdrive_1
from overdrive import overdrive_2
from chorus import flanger
from correlation import corrélation
from pitchdetector import pitchdetection


FORMAT = pyaudio.paFloat32
RATE = 16000
fs= RATE
CHUNK = 1024
RECORD_SECONDS = 10
CHANNELS = 2

p =   pyaudio.PyAudio()

player = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, 
frames_per_buffer=CHUNK)
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)




##Ecoute en temps réel des hauts-parleurs 
for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
    a = np.fromstring(stream.read(CHUNK),dtype=np.float32)
    
    a=flanger(a,1,5,2,1,fs)
    
#    x=overdrive_1(a,75,15.9,15.6,0)
#    x=filtre_butter_passe_haut(x,320,16000)
#    x=filtre_butter_passe_bas(x,1600,16000)
    a=reverb(a,1,16000)
    player.write(a,CHUNK)
    



stream.stop_stream()
stream.close()
p.terminate()