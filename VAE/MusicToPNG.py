import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display

filename=librosa.example('nutcracker')
x=librosa.load(filename)

hop_length = 256

fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
D = librosa.amplitude_to_db(np.abs(librosa.stft(x[0],n_fft=2048,hop_length=hop_length)), ref=np.max)

img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                               sr=x[1], ax=ax[0], hop_length=hop_length)
ax[0].set(title='Linear-frequency power spectrogram')
ax[0].label_outer()