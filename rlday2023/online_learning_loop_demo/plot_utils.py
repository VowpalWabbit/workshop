BLUE = '#415ebf'
PINK = '#ff3ab0'

def plot_ctr(ctrs, labels, *, colors=[BLUE, PINK]):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.xlabel("iterations", fontsize=13)
    plt.ylabel("ctr", fontsize=13)
    plt.ylim([0, 1])

    for ctr, label, color in zip(ctrs, labels, colors):
        plt.plot(ctr, label=label, color=color)
    plt.legend(loc="upper right")
    plt.show()