import numpy
import matplotlib.pyplot as plt

# some starting nodes+edges
adjacency_indices = [[1], [0], [0]]
total_degree = 3
n = 1000
p = [adjacency_indices[i].__len__() / total_degree for i in range(adjacency_indices.__len__())]

for i in range(3, n):
    new_node = []
    adjacency_indices.append([])
    count = 0
    for j in range(adjacency_indices.__len__() - 1):
        if p[j] > numpy.random.uniform():
            new_node.append(j)
            adjacency_indices[j].append(i)
            total_degree += 1
            count += 1
            p[j] = adjacency_indices[j].__len__() / total_degree
    p.append(count / total_degree)

def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x == 0 else x for x in values]


X = [0 for i in range(0, n)]
for a in adjacency_indices:
    X[a.__len__()] += 1
X = [X[i] / total_degree for i in range(X.__len__())]

plt.plot(range(n), zero_to_nan(X), 'ro')
plt.xlim(xmin=0)
plt.show()
