# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:17:06 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from scipy.signal import lfilter
from scipy.signal import butter,filtfilt
from scipy import signal
import soundfile
from scipy.fftpack import fft2, ifft2
L=[[]]

 



#for m in range (1,5):
#    P=[]
#    for i in range (2000):
#        k=np.sin(-np.pi/2+4*np.pi/2000*i)+ass
#        P.append(k)
#        
#        drive=95
#        a=np.sin(((drive+1)/101)*(np.pi/2))
#        k=2*a/(1-a)
#        l=P[i]
#        j=np.absolute(l)
#        P[i]=(((1+k))*l)/((1+k*j))-ass
#    L.append(P)
#    plt.plot(L[m])
#P=[]
#for i in range (2000):
#    k=np.sin(-np.pi/2+4*np.pi/2000*i)
#    P.append(k)
#    j=np.absolute(k)        
#    if j<1/3:
#        P[i]=2*k
#        
#    elif 1/3<k<2/3:
#        P[i]=(3-((2-3* P[i])**2))/3
#        
#    elif -2/3<k<-1/3:
#        P[i]=-((3-((2-3* (-P[i]))**2))/3)
#    elif k<-2/3:
#        P[i]=-(1)
#        
#    else:
#        P[i]=1
#    
#   
#
#
#plt.plot(P)

#x=[]
#
#for i in range (2000):
#    k=np.sin(-np.pi/2+4*np.pi/2000*i)
#    x.append(k)
#    j=np.absolute(k)
#    if d==0:
#        x[i]=x[i]
#    elif k==0:
#        x[i]=0
#    else:
#        x[i]=(k/j)*(1-np.exp(-(d*(k**2))/j))
#x = 0.99 * x / max(abs(x))
#
#plt.plot(x)


from overdrive import overdrive_1


L=[L]
for m in range (5):
    P=[]
    
    for i in range (2001):
        
        k=np.sin(-np.pi/2+4*np.pi/2001*i)
        P.append(k)
    y=overdrive_1(P,100+10*m,15.9,15.6,0)
    plt.plot( y, label='disto='+str(10*m))   
    
        
                
            

plt.legend()
            

#P=[]
#for i in range (2000):
#    k=np.sin(-np.pi/2+4*np.pi/2000*i)
#    P.append(k)
#    j=np.absolute(k)        
#    if j<1/3:
#        P[i]=2*k
#        
#    elif 1/3<k<2/3:
#        P[i]=(3-((2-3* P[i])**2))/3
#        
#    elif -2/3<k<-1/3:
#        P[i]=-((3-((2-3* (-P[i]))**2))/3)
#    elif k<-2/3:
#        P[i]=-(1)
#        
#    else:
#        P[i]=1
#    
#   
#
#
#plt.plot(P)