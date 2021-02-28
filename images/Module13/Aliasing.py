import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
idx = 0
n_harm = 2
freqs = [(2, 10), (1, 50)]
for N in range(300, 10, -1):
    plt.clf()
    y = np.zeros(N)
    for (A, k) in freqs:
        y += A*np.cos(2*np.pi*k*np.arange(N)/N)
    X = np.fft.fft(y)/N
    plt.subplot(212)
    plt.stem(np.abs(X))
    plt.xlabel("Frequency Index")
    plt.ylabel("Amplitude")
    plt.ylim([-0.1, 1.6])
    plt.title("Complex DFT Magnitudes")
    
    plt.subplot(211)
    plt.plot(y)
    plt.title("N = {}".format(N))
    plt.ylim([-5, 5])
    pause = 1
    if N == freqs[-1][1]*2:
        pause = 10
    
    for k in range(pause):
        plt.savefig("{}.png".format(idx))
        idx += 1