import matplotlib.pyplot as plt

pair = []


def collatz(x: int, index: int):
    if x == 1:
        return
    elif x % 2 == 0:
        pair.__getitem__(index).__getitem__(1).append(int(x / 2))
        collatz(x / 2, index)
    else:
        pair.__getitem__(index).__getitem__(1).append(int(3 * x + 1))
        collatz(3 * x + 1, index)


def printPair():
    for a, b in pair:
        print(a, b)


def groupPair(x: int):
    for a, b in pair:
        if b.__contains__(x):
            print(a, b)


def plotPairByGroup(x: int):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for a, b in pair:
        if b.__contains__(x):
            ax1.plot(b)

    #plt.show()
    plt.savefig('groupPlot')


def plotPair():
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    for a, b in pair:
        ax1.plot(b)

    plt.show()


def main(startIndex: int, endIndex: int):
    for i in range(startIndex, endIndex):
        pair.append((i, []))
        collatz(i, i - startIndex)

    groupPair(5)
    plotPairByGroup(5)
