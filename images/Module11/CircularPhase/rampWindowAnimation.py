import numpy as np
import matplotlib.pyplot as plt

def plotPosNeg(s):
    idxn = np.arange(len(s))
    sn = s[s < 0]
    idxn = idxn[s < 0]
    sp = s[s >= 0]
    idxp = np.arange(len(s))
    idxp = idxp[s >= 0]
    if len(idxp) > 0:
        plt.stem(idxp, sp, 'r', markerfmt='ro')
    if len(idxn) > 0:
        plt.stem(idxn, sn, 'b')

if __name__ == '__main__2':
    N = 31
    for i in range(N):
        f = np.floor((i+1)/2)
        plt.subplot(6, 6, i)
        y = np.cos(np.arange(N)*2*np.pi*f/N)
        if i%2 == 0:
            y = np.sin(np.arange(N)*2*np.pi*f/N)
        plt.plot(y)
        plt.axis('off')
    plt.show()

if __name__ == '__main__':
    N = 1001
    t = np.linspace(0, 2*np.pi, N)
    #x = np.exp(-(np.array(np.arange(N), dtype=np.int64)-150.0)**2/(10.0**2))
    a0 = 0.21557895
    a1 = 0.41663158
    a2 = 0.277263158
    a3 = 0.083578947
    a4 = 0.006947368
    w = 1#np.sin(0.5*t)#a0 - a1*np.cos(t) + a2*np.cos(2*t) - a3 * np.cos(3*t) + a4*np.cos(4*t)
    plt.figure(figsize=(12, 6))
    plot_lim = 10
    for shift in range(1, N):
        x = np.cos(3.5*t)
        x[x == 0] = 1
        x = x*w
        y = 0*x
        y[0:shift] = x[-shift:]
        y[shift:] = x[0:-shift]
        x = y
        basis = []
        coeffs = []
        zgt = 0*x
        sines = []
        cosines = []
        strings = []
        for i in range(N):
            f = np.floor((i+1)/2)
            y = np.cos(np.arange(N)*2*np.pi*f/N)
            if i%2 == 1:
                y = np.sin(np.arange(N)*2*np.pi*f/N)
            basis.append(y)
            coeffs.append(np.sum(y*x)/(N/2))
            zgt += coeffs[i]*basis[i]
            if i == 0:
                strings.append('DC')
                continue
            if i%2 == 1:
                sines.append(coeffs[i])
                strings.append('Sine %i'%f)
            else:
                cosines.append(coeffs[i])
                strings.append('Cosine %i'%f)
        
        z = np.concatenate((x[None, :], x[None, :], x[None, :]), 1).flatten()
        cosines = np.array(cosines)
        sines = np.array(sines)
        

        plt.clf()
        plt.subplot2grid((2, 4), (0, 0), colspan=4, rowspan=1)
        plt.plot(z)
        z[0:N] = 0
        z[-N:] = 0
        plt.plot(z)
        plt.plot([N, N], [0, 1.0], 'C1')
        plt.plot([2*N, 2*N], [0, 1.0], 'C1')
        plt.title('Signal')
        plt.subplot(245)
        plt.stem(cosines)
        plt.ylim([-1.1, 1.1])
        plt.xlim([-0.5, plot_lim+0.5])
        plt.title('Cosines')
        plt.xlabel("Frequency Index")
        plt.ylabel("Amplitude")
        plt.subplot(246)
        plt.stem(sines)
        plt.ylim([-1.1, 1.1])
        plt.xlim([-0.5, plot_lim+0.5])
        plt.title('Sines')
        plt.xlabel("Frequency Index")
        plt.ylabel("Amplitude")
        plt.subplot(247)
        amps = np.sqrt(np.array(sines)**2 + np.array(cosines)**2)
        phases = np.arctan2(sines, cosines)
        plt.stem(amps)
        plt.xlim([-0.5, plot_lim+0.5])
        plt.title('Amplitude')
        plt.tight_layout()
        plt.subplot(248)
        plt.stem((amps > 1e-2)*phases, use_line_collection=True)
        plt.ylim([-np.pi-0.1, np.pi+0.1])
        plt.xlim([-0.5, plot_lim+0.5])
        plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ["$-\\pi$", "$\\pi/2$", "0", "$\\pi/2$", "$\\pi$"])
        plt.xlabel("Frequency Index")
        plt.ylabel("Phase (Radians)")
        plt.title("Phase")

        plt.savefig("Ramp%i.png"%shift, dpi = 120, bbox_inches='tight')

