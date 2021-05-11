# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

plt.plot(input_data) 


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
#output_data = noise + 0*output_data





def disto(x,d):
    for i in range (n):
        k=x[i]
        j=np.absolute(k)
        if d==0:
            x[i]=x[i]
        elif k==0:
            x[i]=0
        else:
            x[i]=(k/j)*(1-np.exp(-(d*(k**2))/j))
    return x





def overdrive(x,drive,fc1,fc2,ass):
    #filtre passe bas
    fc=1/fc1
    inputfpb_data= x
    
    for i in range(1,n):
        x[i]= fc*x[i-1]+inputfpb_data[i]
        
    ##filtre passe haut
    fc=-1/fc2
    inputfpb_data= x
    
    for i in range(1,n):
        x[i]= fc*x[i-1]+inputfpb_data[i]
        
       
    for i in range (n):
        x[i]=x[i]+ ass
        a=np.sin(((drive+1)/101)*(np.pi/2))
        k=2*a/(1-a)
        l=x[i]
        j=np.absolute(l)
        if drive==0:
            x[i]=x[i] - ass
        elif l==0:
            x[i]=0 - ass
        else:
            x[i]=((1+k)*l)/(1+k*j)+l - ass
    return x




def overdrive_2(x,gain,ass):            
    for i in range (n):
        x[i]=x[i]*gain-ass
        j=np.absolute(x[i])  
        
        if j<1/3:
            x[i]=2*x[i]+ass
            
        elif 1/3<x[i]<2/3:
            
            x[i]=(3-((2-3* x[i])**2))/3+ass
            
        elif -2/3<x[i]<-1/3:
            x[i]=-((3+ass-((2-ass-3* (-x[i]))**2))/3)
        elif x[i]<-2/3:
            x[i]=-1+ass
            
        else:
            x[i]=1+ass
    return x

output_data = overdrive_2(input_data,1,0)
#output_data = overdrive(input_data,80,15.9,15.6,0)
output_data = 0.99 * output_data / max(abs(output_data))

plt.plot(output_data) 

#output_data = output_data + overdrive(output_data,65,15.9,15.6,0.2)
#output_data = output_data + overdrive(output_data,65,15.9,15.6,0.3)
#output_data = output_data + overdrive(output_data,65,15.9,15.6,0.4)

####flanger
#
#A = 50
#data_flanger=output_data
#rate = 0.2
#manual = 10
#period = 1/fs
#l=1
#p=len(output_data)-A-manual
#
#for i in range (p):
#    t=int(A*np.sin(2*np.pi*i*rate*period))
#    output_data[i] = output_data[i] + l*data_flanger[(i + manual + t)]
#
#output_data = 0.99 * output_data / max(abs(output_data))
#
#A = 50
#
#rate = 0.5
#manual = 10
#period = 1/fs
#l=1
#p=len(output_data)-A-manual
#
#for i in range (p):
#    t=int(A*np.sin(2*np.pi*i*rate*period))
#    output_data[i] = output_data[i] + l*data_flanger[(i + manual + t)]

###tremolo
#ftr=4
#r=0.5
#
#for i in range(n):
#    output_data[i]=output_data[i]+r*output_data[i]*np.sin(2*np.pi*ftr*i/fs)
#output_data = 0.99 * output_data / max(abs(output_data))


###delay
#a=0.5
#d=5000
#input_data_delay=output_data
#for i in range(d,n) :
#  output_data[i]=a*output_data[i-d]+ input_data_delay[i]
  
  
##reverb 
#a=0.5
#d=int(2*fs*0.02)
#input_data_reverb=output_data
#
#for i in range(d,n) :
#  output_data[i]= a*output_data[i-d] + input_data_reverb[i]

###filtre passe bas
#fc=1/320
#inputfpb_data= output_data
#
#for i in range(1,n):
#    output_data[i]= fc*output_data[i-1]+inputfpb_data[i]
#    
###filtre passe haut
#fc=-1/1160
#inputfpb_data= output_data
#
#for i in range(1,n):
#    output_data[i]= fc*output_data[i-1]+inputfpb_data[i]

##filtre butter passe bas
fc = 320  # Cut-off frequency of the filter
w = fc / (fs / 1) # Normalize the frequency
b, a = signal.butter(2, w, 'low')
output_data = signal.filtfilt(b, a, output_data)

##filtre butter passe haut
fc = 1160  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(2, w, 'highpass')
output_data = signal.filtfilt(b, a, output_data)

bk=min(output_data)
ak=max(output_data)
output_data = 0.99 * output_data / max(abs(output_data))
bk2=min(output_data)
ak2=max(output_data)

wavfile.write(output_file, int(fs), output_data)
