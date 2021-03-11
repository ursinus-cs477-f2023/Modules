import numpy as np
import librosa

xs, sr = librosa.load("beatles.wav", sr=8000)
xs = xs[0:sr*4]
s = "x = np.array(["
for x in xs:
    s += "{},".format(x)
s = s[0:-1] + "])"
print(s)
