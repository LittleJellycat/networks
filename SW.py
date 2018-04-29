import numpy
import matplotlib.pyplot as plt

n = 40
beta = 0.2
wires_number = 5
edges = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(wires_number):
        edges[i][(i + j + 1) % n] = 1
for i in range(n):
    for j in range(n):
        if edges[i][j] == 1:
            if numpy.random.uniform() < beta:
                while True:
                    new_i = numpy.random.randint(0, 10)
                    new_j = numpy.random.randint(0, 10)
                    if edges[new_i][new_j] == 0:
                        edges[i][j] = 0
                        edges[j][i] = 0
                        edges[new_i][new_j] = 1
                        edges[new_j][new_i] = 1
                        break
degrees = [numpy.sum(edges[i]) for i in range(n)]


def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x == 0 else x for x in values]


X = [0 for i in range(0, n)]
for i in range(n):
    X[degrees[i]] += 1
X = [X[i] / n for i in range(X.__len__())]

plt.plot(range(n), zero_to_nan(X), 'ro')
plt.xlim(xmin=0)
plt.xlabel('k')
plt.ylabel('P(k)')
plt.show()
