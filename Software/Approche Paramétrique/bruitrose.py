# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:58:27 2021

@author: duwat
"""

import numpy as np
import scipy.io.wavfile as wavfile
from scipy.signal import lfilter
from scipy.signal import butter,filtfilt
from scipy import signal
import soundfile
from scipy.fftpack import fft2, ifft2
import matplotlib.pyplot as plt
import math
import cmath




##bruit rose
def pink_noise(f_ref, f_min, f_max, length, f_sample):
    aliasfil_len = 10000
    fil_Time = aliasfil_len * 1/f_sample
    L = length + 2 * fil_Time
    f_low = 1 / L
    f_high = f_sample
    T = f_low * 2 * np.pi
    k_max = int(f_high / f_low / 2) + 1
    print(k_max)

    # Create frequencies
    f = np.array([(k * T)/(2 * np.pi) for k in range(0, k_max)])

    # Create 1/f noise amplitude in band
    C = np.array([(1 / f[k] if (f[k] >= f_min and f[k] <= f_max) else 0)
                  for k in range(0, k_max)], dtype='complex')
    C[0] = 0
    # Create random phase in band
    Phase = np.array([(np.random.uniform(0, np.pi)
                       if (f[k] >= f_min and f[k] <= f_max)
                       else 0)
                      for k in range(0, k_max)])

    Clist_neg = list()
    Clist_pos = list()
    for k in range(-k_max + 1, -1):
        Clist_neg.append(C[-k] * cmath.exp(-1j * Phase[-k]))
    for k in range(0, k_max):
        Clist_pos.append(C[k]  * cmath.exp( 1j * Phase[k] ))

    CC = np.array(Clist_pos + Clist_neg, dtype='complex')

    # Scale to max amplitude
    maxampl = max(abs(CC))
    CC /= maxampl

    tsig = np.fft.ifft(CC)
    sig = np.real(np.sign(tsig)) * np.abs(tsig)

    # Filter aliassing
    sig = sig[aliasfil_len:-aliasfil_len]

    # clip to maximum signal and
    # correct for amplitude at reference frequency
    if f_ref > ((f_max + f_min) / 2):
        print("WARNING: f_ref ({} Hz) should be smaller or equal to the mid "
              "between {} Hz and {} Hz "
              "to prevent clipping.\n"
              "f_ref changed to {} Hz"
              .format(f_ref,
                      f_min,
                      f_max,
                      ((f_max + f_min) / 2)))
        f_ref = ((f_max + f_min) / 2)
    maxampl = max(np.abs(sig))
    sig = sig / maxampl * f_ref / ((f_max + f_min) / 2)

    halfway = int(len(sig) / 2)
    # sign invert second part for a good connection,
    # it is the mirror of the first half
    sig2nd = -1 * sig[halfway:]
    sigc = np.concatenate((sig[0:halfway], sig2nd))
    # average middle point, but second point sign inverted
    sigc[halfway] = (sig[halfway-1] - sig[halfway+1])/2

    return(sigc)


length = 10.0  # seconds
f_sample = 44100  # Hz

f_ref = 3000  # Hz, The frequency for max amplitude

f_min = 10  # Hz
f_max = 20000  # hz

sig = pink_noise(f_ref, f_min, f_max, length, f_sample)



p = 0
for x in sig:
    p += abs(x)
rms = math.sqrt(p/len(sig))
print("rms = {:f}, {:5.1f} dB".format(rms, 20 * math.log10(rms)))

print("Length of time signal: {} samples".format(len(sig)))
print("Time signal: ", sig)
x = sig * (2**15 - 1)

wavfile.write("test.wav", f_sample, np.array(x, dtype=np.int16))