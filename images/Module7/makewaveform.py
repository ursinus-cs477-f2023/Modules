import librosa
import numpy as np

ys, sr = librosa.load("gameover.wav", sr=8000)
print("[", end='')
for i, y in enumerate(ys):
    print("%.3g"%y, end='')
    if i < len(ys)-1:
        print(",", end='')
print("]")
