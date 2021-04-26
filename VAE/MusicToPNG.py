import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display

filename=librosa.example('nutcracker')
x=librosa.load(filename)

hop_length = 256

fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
D = librosa.amplitude_to_db(np.abs(librosa.stft(x[0],n_fft=2048,hop_length=hop_length)), ref=np.max)

img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                               sr=x[1], ax=ax1, hop_length=hop_length)
ax1.set(title='Linear-frequency power spectrogram')
ax1.label_outer()

librosa.display.waveplot(x[0], sr=x[1], ax=ax2)
