# import numpy as np
# import networkx as nx
# import pylab as plt
#
# # A = np.array([[0,0,1,0],[1,0,0,0],[1,0,0,1],[1,0,0,0]])
# A = np.array([
#     [2,1,0,0,1,0],
#     [1,0,1,0,1,0],
#     [0,1,0,1,0,0],
#     [0,0,1,0,1,1],
#     [1,1,0,1,0,0],
#     [0,0,0,0,0,0]
#     ])
# G = nx.DiGraph(A)
#
# pos = [[0,0], [0,1], [1,0], [1,1],[0,2],[2,2]]
# # pos = [[0,0,0], [0,0,1], [0,1,0], [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
# nx.draw(G,pos)
# plt.show()

import numpy as np
import networkx as nx
import pylab as plt

# A = np.array([[0,0,1,0],[1,0,0,0],[1,0,0,1],[1,0,0,0]])

# A=[2,1,0,0,1,0]
# B=[1,0,1,0,1,0]
# C=[0,1,0,1,0,0]
# D=[0,0,1,0,1,1]
# E=[1,1,0,1,0,0]
# F=[0,0,0,0,0,0]

# graph = np.array([
#     [2,1,0,0,1,0],
#     [1,0,1,0,1,0],
#     [0,1,0,1,0,0],
#     [0,0,1,0,1,1],
#     [1,1,0,1,0,0],
#     [0,0,0,0,0,0]
#     ])
graph = np.array([
    [0,1,1,0,1,1],
    [1,0,1,1,0,0],
    [1,1,0,1,1,0],
    [0,1,1,0,1,0],
    [1,0,1,1,1,0],
    [1,0,0,0,1,0]
    ])

graff = ([
    [0,1,1,0,1,1],
    [1,0,1,1,0,0],
    [1,1,0,1,1,0],
    [0,1,1,0,1,0],
    [1,0,1,1,1,0],
    [1,0,0,0,1,0]
    ])

for i in graff:



G = nx.DiGraph(graph)

# nx.draw(G,pos)
# plt.show()

pos = nx.spring_layout(G)
nx.draw(G, pos, font_size=14, with_labels=False)
# for p in pos:  # raise text positions
#     pos[p][1] += 0.07
nx.draw_networkx_labels(G, pos)
plt.show()
