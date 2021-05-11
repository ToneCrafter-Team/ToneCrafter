# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:56:06 2021

@author: duwat
"""


import librosa
import librosa.display




from filtres import filtre_passe_bas
from filtres import filtre_passe_haut
from filtres import filtre_butter_passe_bas
from filtres import filtre_butter_passe_haut
from disto import disto
from timeeffect import reverb
from overdrive import overdrive_1
from overdrive import overdrive_2
from chorus import chorus
from correlation import corrélation
from pitchdetector import pitchdetection



x, sr = librosa.load('Bohemian Rhapsody.wav',offset=2)
fs=sr

def effectdetection(x):
    X=[]
    Coeff=[]
    
    Notemes=[]
    NumeroNote=[]
    corr=10000000
    #découpage en signaux de 50ms :
    s=int((fs*50)/1000) #liste de 50ms
    for i in range (5):
        
        xi=[]
        for j in range (s):
            a=(100*i+j)
            xij=x[a]
            xi.append(xij)
            
        X.append(xi) 
        xi=[]
    
    print(X)      
            
            
#    reconnaissance de la note :
    for i in range (len(X)):
        
        Notemes.append(pitchdetection(X[i])[0])#une note peut souvent se faire de plusieurs manières sur une guitare
        
        print(Notemes)
        
        NumeroNote.append(pitchdetection(X[i])[1])
#        print(pitchdetection(X[i])[1])
#    chargement de la note clean correspondante :
        for i in range(len(Notemes)):
            nom=NumeroNote[i]
            print(nom)
            Corr=[]
            y, sr = librosa.load(str(nom)+'.wav', offset=1.0, duration=s*fs)
            Corr.append(corrélation(x,y))
        p=Corr.index(min(Corr))
        y=Corr[p]  #le son le plus proche est choisi  
    
##    MTN ON VA APPLIQUER LES DIFFERENTS EFFETS
#    
#    print(Coeff)
#    for i in range(1):
#        x=X[i]
#        print(Coeff)
#        for i3 in range (10):
#            for i4 in range (10):
#                
#                x=overdrive_1(x,i3*10,15.9,15.6,-0.5+0.1*i4)
#                
#                for i5 in range (10):
#                    for i6 in range (10):
#                        
#                        x=overdrive_2(x, 0.2*i5 , -0.5+0.1*i6)
#                        
#                        for i7 in range (10):
#                            
#                            x=disto(x,i7*10)
#                            
#                            for i8 in range (10):
#                                
#                                x=filtre_passe_bas(x,4*10**(i8+1))
#                                
#                                for i9 in range (10):
#                                    
#                                    x=filtre_passe_haut(x,4*10**(i9+1))
#                                    
#                                    for i10 in range (10):
#                                
#                                        x=filtre_butter_passe_bas(x,4*10**(i10+1))
#                                
#                                        for i11 in range (10):
#                                    
#                                            x=filtre_butter_passe_haut(x,4*10**(i11+1))
#                                            
#                                            for i12 in range (10):
#                                                for i13 in range (10):
#                                                    for i14 in range (10):
#                                                        
#                                                        chorus(x,50,50,50,0.1*i12,0.1*i13,0.1*i14,10,1,1,1,fs)
#                                                        
#                                                        for i15 in range (10):
#                                                            
#                                                            reverb(x,0.1*i15,fs)
#                                                            c=corrélation(x,y)
#                                                            if c<corr:
#                                                                corr=c
#                                                                Coeff.append([i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15])
#                                                                print(Coeff)
                                        
                                
                                
                                
                                
        
        
    
    return y