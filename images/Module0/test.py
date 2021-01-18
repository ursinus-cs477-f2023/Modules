import subprocess
import sys
# Install packages we'll need in the course
for package in ["librosa", "essentia"]:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
# Test librosa stft with chirp
sr = 22050
t = np.arange(sr*2)
y = np.cos(2*np.pi*(t/1000)**2*t/sr)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(D, y_axis='linear', x_axis='time', sr=sr)
plt.show()