import numpy as np
import matplotlib.pyplot as plt


def plot_phasor(A, f, phi, t, N):
    tt = np.linspace(0, t, int(N*t))
    c = A*np.cos(2*np.pi*f*tt+phi[0])
    s = A*np.sin(2*np.pi*f*tt+phi[0])
    plt.subplot2grid((10, 1), (0, 0), 9, 1)
    plt.plot(c, s)
    plt.arrow(0, 0, c[-1], s[-1], width=0.01, color='C1')
    plt.scatter([c[0], c[-1]], [s[0], s[-1]], c='C1')
    txt = "${}e^(i 2 \\pi * {} * {:.3f} + {})$".format(A, f, tt[-1], phi[1])
    plt.text(c[-1]*0.5, s[-1]*0.5, txt)
    plt.axis('equal')
    plt.xlim([-3, 3])
    plt.ylim([-3, 3])
    txt = "${} \cos(2 \\pi * {} * {:.3f} + {})$".format(A, f, tt[-1], phi[1])
    txt += "\n$+ i{}\\sin(2 \\pi * {} * {:.3f} + {})$".format(A, f, tt[-1], phi[1])
    plt.title(txt)
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.subplot2grid((10, 1), (9, 0), 1, 1)
    plt.arrow(0, 0, c[-1], 0)
    plt.xlim([-3, 3])
    plt.axis('off')


def plot_phasors(As, fs, phis, t, N, show_title=True):
    tt = np.linspace(0, t, int(N*t)+1)
    c = np.zeros(len(tt))
    s = np.zeros(len(tt))
    x = 0
    y = 0
    plt.subplot2grid((10, 1), (0, 0), 9, 1)
    txt = ""
    i = 0
    for A, f, phi in zip(As, fs, phis):
        c += A*np.cos(2*np.pi*f*tt+phi[0])
        s += A*np.sin(2*np.pi*f*tt+phi[0])
        plt.arrow(x, y, c[-1]-x, s[-1]-y, width = 0.03)
        x = c[-1]
        y = s[-1]
        if i > 0:
            txt += " + "
        txt += "${} \cos(2 \\pi * {:.3f} * {:.3f} + {})$\n".format(A, f, tt[-1], phi[1])
        i += 1
    plt.plot(c, s)
    plt.scatter([c[0], c[-1]], [s[0], s[-1]], c='C1')
    plt.axis('equal')
    plt.xlim([-6, 6])
    plt.ylim([-6, 6])
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    if show_title:
        plt.title(txt)
    plt.subplot2grid((10, 1), (9, 0), 1, 1)
    plt.arrow(0, 0, c[-1], 0)
    plt.xlim([-5, 5])
    plt.axis('off')
    return c


H = 10
As = []
fs = []
phis = [(np.pi/2, "\\pi/2")]*H
for i in range(H):
    As.append(2/(2*i+1))
    fs.append(1+2*i)

As = [3]
fs = [2]
phis = [(-np.pi/2, "")]

plt.figure(figsize=(8, 8))
N = 10000
for i, t in enumerate(np.linspace(0, 1, 100)):
    plt.clf()
    c = plot_phasors(As, fs, phis, t, N, False)
    plt.savefig("{}.png".format(i), bbox_inches='tight')
plt.figure(figsize=(8, 4))
plt.plot(c)
plt.savefig("Signal.svg", bbox_inches='tight')
