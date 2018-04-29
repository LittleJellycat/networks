import numpy
import matplotlib.pyplot as plt

p = 0.7
n = 100
X = []
for k in range(n):
    edges = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            if numpy.random.uniform() < p:
                edges[i][j] = 1
                edges[j][i] = 1
    degrees = [numpy.sum(edges[m]) for m in range(n)]
    index = numpy.max(degrees)
    p_k = [0 for i in range(n+1)]
    for d in degrees:
        p_k[d] += 1
    p_k = [p_k[i] / n for i in range(n)]
    X.append(p_k)


def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x == 0 else x for x in values]


X = numpy.transpose(X)
X = [numpy.average(X[m]) for m in range(n)]

plt.plot(range(n), zero_to_nan(X), 'ro')
plt.xlim(xmin=0, xmax=n)
plt.show()
