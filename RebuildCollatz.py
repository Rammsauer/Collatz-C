import matplotlib.pyplot as plt

rebuildedCollatz = [(0, [])]


def printCollatz():
    for a, b in rebuildedCollatz:
        if a == 3:
            print(b)


def plotPairByRebuild():
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for a, b in rebuildedCollatz:
        if a == 3:
            ax1.plot(b)

    # plt.savefig("firstPointLinkedBo")
    plt.show()


def listContainsArray(array):
    for a, b in rebuildedCollatz:
        if b == array:
            return True
        else:
            return False


def addLinkArray(array):
    temp = []
    for a in array:
        temp.append(a)
    return temp


def rebuildCollatzByNumber(x: int, array, index: int, withLink: bool):
    if listContainsArray(array):
        return

    if x > 10000:
        rebuildedCollatz.append((index, array))
        return

    if ((x - 1) / 3) % 2 == 1:
        if not array.__contains__(int((x - 1) / 3)):
            temp = []
            if withLink:
                temp = addLinkArray(array)
            temp.append(int((x - 1) / 3))
            rebuildCollatzByNumber(int((x - 1) / 3), temp, index + 1, withLink)

    array.append(x * 2)
    rebuildCollatzByNumber(x * 2, array, index, withLink)
