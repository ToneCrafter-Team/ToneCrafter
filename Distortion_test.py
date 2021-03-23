import ddsp
import ddsp.training
from ddsp.colab.colab_utils import (specplot, DEFAULT_SAMPLE_RATE)
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import sounddevice as sd

import librosa


sample_rate = DEFAULT_SAMPLE_RATE  # Default_sample_rate = 16000


# Constants
n_frames = 1000
hop_size = 64
n_samples = n_frames * hop_size


#### Additive controls

# Amplitude [batch, n_frames, 1].
amps = np.linspace(1.0, -3.0, n_frames)
amps = amps[np.newaxis, :, np.newaxis]


# Harmonic Distribution [batch, n_frames, n_harmonics].
n_harmonics = 5
harmonic_distribution = np.ones([n_frames, 1]) * np.linspace(1.0, -1.0, n_harmonics)[np.newaxis, :]
harmonic_distribution = harmonic_distribution[np.newaxis, :, :]


# Fundamental frequency in Hz [batch, n_frames, 1].
f0_hz = 440.0 * np.ones([1, n_frames, 1])


### Filtered Noise controls
# Magnitudes [batch, n_frames, n_magnitudes].
n_filter_banks = 20
magnitudes = np.linspace(-1.0, -4.0, n_filter_banks)[np.newaxis, np.newaxis, :]
magnitudes = magnitudes + amps 



# Create synthesizer object.
additive_synth = ddsp.synths.Additive(n_samples=n_samples,
                                      scale_fn=ddsp.core.exp_sigmoid,
                                      sample_rate=sample_rate)

# Generate some audio.
audio = additive_synth(amps, harmonic_distribution, f0_hz)

time = np.linspace(0, n_samples / sample_rate, n_frames)
time1 = np.linspace(0, 1, 64000)

plt.figure(figsize=(18, 4))
plt.subplot(131)
plt.plot(time, amps[0, :, 0])
plt.xticks([0, 1, 2, 3, 4])
plt.title('Amplitude')

plt.subplot(132)
plt.plot(time, harmonic_distribution[0, :, :])
plt.xticks([0, 1, 2, 3, 4])
plt.title('Harmonic Distribution')

plt.subplot(133)
plt.plot(time, f0_hz[0, :, 0])
plt.xticks([0, 1, 2, 3, 4])
_ = plt.title('Fundamental Frequency')



#Plot the audio signal 
plt.figure(figsize=(18, 4))
plt.plot(time1, np.transpose(audio.numpy()))
plt.xlim([0,0.01])


#Listen to the audio and visualize the spectrogram
#sd.play(np.transpose(audio),sample_rate)
specplot(audio)



#First try of a distortion function 
def distortion(A,audio):
    k = 2*A/(1-A)
    audio_out = (1+k)*abs(audio)/(1+k*audio)
    #Hsd.play(np.transpose(audio_out),sample_rate)
    return audio_out

#sd.play(np.transpose(distortion(0.2,audio)),sample_rate)
specplot(distortion(0.2,audio))



#Another try of a Distortion... 
audio_dist=audio
audio_dist_np=np.empty_like(audio_dist.numpy())
pregain=1
treshold=0.03
for i in range (n_frames*hop_size):

    audio_dist_np[0][i]=pregain*audio_dist.numpy()[0][i]
    if audio_dist.numpy()[0][i]>treshold:
        audio_dist_np[0][i]=treshold
    if audio_dist.numpy()[0][i]<-treshold:
        audio_dist_np[0][i]=-treshold
        #print("Set to -0.4")


#Listen to the audio and visualize the audio with distortion and it's spectrogram
#sd.play(np.transpose(audio_dist_np),sample_rate)

plt.figure(figsize=(18, 4))
plt.plot(time1, np.transpose(audio_dist_np))
plt.xlim([0,0.01])

specplot(audio_dist_np)
