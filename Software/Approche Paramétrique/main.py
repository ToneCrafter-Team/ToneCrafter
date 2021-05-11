# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:56:49 2021

@author: duwat
"""
import numpy as np
import scipy.io.wavfile as wavfile

import matplotlib.pyplot as plt

from scipy.io.wavfile import write

from filtres import *
from disto import *
from overdrive import *
from chorus import *


'guitar2.wav'
input_file = 'guitar2.wav'
output_file = 'output.wav'

fs, input_data = wavfile.read(input_file, mmap=True)

# convert to float
max_value = float(-np.iinfo(input_data.dtype).min)
input_data = input_data.astype('float32') / max_value

# convert to mono if not already
if len(input_data.shape) > 1:
    input_data = np.mean(input_data, axis=1)
    
    
    
input_data = input_data.flatten()
n=len(input_data)
output_data = np.zeros(len(input_data))

x=input_data
plt.plot(x)
plt.show

x1=overdrive_1(x,10,80,15.9,15.6,0)





#plt.plot(x)
#plt.show

#x=filtre_passe_bas(x,530)

#plt.plot(x)
#plt.show

#disto
#
#chorus

#tremolo
#
#delay
#
#reverb
plt.plot(x1)
plt.show
write("output.wav", 22050, x)

s=0
for i in range (n):
    s=s+(x1[i]-x[i])**1
print(np.sqrt(s)/len(input_data))
output_data=x1
wavfile.write("output.wav", fs, np.array(output_data, dtype=np.int16))