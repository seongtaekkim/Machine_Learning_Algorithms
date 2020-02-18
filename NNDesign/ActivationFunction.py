import matplotlib.pyplot as plt


def hardlim():
    x = range(-100, 100)
    y = []

    for i in x:
        if i >= 0:
            y.append(1)
        else:
            y.append(0)

    plt.plot(x, y)
    plt.show()

hardlim()