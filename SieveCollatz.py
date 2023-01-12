import RebuildCollatz as rbCollatz
import NewCollatz as nwCollatz

matrix = []


# works for 1-100
def initMatrix():
    for i in range(1, 102):
        matrix.append(i)


def printMatrix():
    for i in range(len(matrix)):
        if (i+1) % 10 == 0:
            if matrix[i] == -1:
                print(f'    \n', end='')
            else:
                print(f' {matrix[i]} \n', end='')
        else:
            if matrix[i] == -1:
                print(f'    ', end='')
            elif i < 10:
                print(f'  {matrix[i]} ', end='')
            elif matrix[i] == 101:
                print()
            else:
                print(f' {matrix[i]} ', end='')


def removeCollatz(array):
    for a, b in array:
        print(b)
        for i in range(len(matrix)):
            for temp in range(len(b)):
                if b[temp] > 100:
                    break
                elif matrix[i] == b[temp]:
                    matrix[i] = -1
        printMatrix()


initMatrix()

#rbCollatz.rebuildCollatzByNumber(1, [1], 0, True)
#rbCollatz.rebuildedCollatz.sort()

nwCollatz.rebuildCollatzByMod(1, 0)
nwCollatz.l.sort()

removeCollatz(nwCollatz.l)

