import math

pair = []


def traceNumber(x):
    n = math.log(x, 2)
    logs = []
    pair.append(x)

    for i in range(math.floor(n)):
        logs.append(math.pow(2, i))

    logs.reverse()

    while not n.is_integer():
        for i in logs:
            if (x / i).is_integer():
                pair.append(x/i)
                traceNumber((x / i)*3+1)
                return


traceNumber(30)
print(pair)
