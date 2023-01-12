import math
import matplotlib.pyplot as plt

l = [(0, [])]


def printArray():
    for a, b in l:
        print(f'{a} {b}')


def getNumberArray(m):
    temp = []
    for i in range(0, 8):
        temp.append(m * math.pow(2, i))
    return temp


def checkIfArrayExists(array):
    exists = False
    for a, b in l:
        if b.__eq__(array):
            exists = True

    return exists


def isNumberInArray(n):
    exists = False
    for a, b in l:
        if b.__contains__(n):
            exists = True

    return exists


def plotPairByRebuild():
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for a, b in l:
        ax1.plot(b, "bo")

    # plt.savefig("firstPointLinkedBo")
    plt.show()


def rebuildCollatzByMod(n, index):
    array = []
    for i in range(0, 8):
        array.append(n * math.pow(2, i))

    if not checkIfArrayExists(array):
        l.append((index, array))

    for m in array:
        if m < 50:
            for k in range(0, 8):
                if m % 3 == 1:
                    futureBreak = ((m * math.pow(4, k)) - 1) / 3
                    if not isNumberInArray(futureBreak):
                        rebuildCollatzByMod(futureBreak, index + 1)
                elif m % 3 == 2:
                    futureBreak = ((m * math.pow(2, (2 * k + 1))) - 1) / 3
                    if not isNumberInArray(futureBreak):
                        rebuildCollatzByMod(futureBreak, index + 1)
                elif m % 3 == 0:
                    if not checkIfArrayExists(array):
                        l.append((index, getNumberArray(m)))
                else:
                    print(end="")
        else:
            return


rebuildCollatzByMod(1, 0)
l.sort()
printArray()
plotPairByRebuild()