autocorr = np.zeros(len(novfn)*2)
times = np.arange(len(autocorr))*hop_length/sr
plt.figure(figsize=(10, 7))
for shift in range(len(novfn)):
    x1 = np.zeros(len(novfn)*2)
    x2 = np.zeros_like(x1)
    x1[0:len(novfn)] = novfn
    x2[shift:shift+len(novfn)] = novfn
    autocorr[shift] = np.sum(x1*x2)
    plt.clf()
    plt.subplot(211)
    plt.plot(times, x1)
    plt.plot(times, x2)
    plt.title("Shift by {:.3f} Seconds".format(times[shift]))
    plt.subplot(212)
    plt.plot(times, autocorr)
    plt.stem([times[shift]], [autocorr[shift]])
    plt.xlabel("Shift (Seconds)")
    plt.ylabel("Autocorrelation")
    plt.tight_layout()
    plt.savefig("{}.png".format(shift), facecolor='white')
