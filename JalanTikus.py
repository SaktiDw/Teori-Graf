import networkx as nx
import pylab as plt
import re

#default
V = ['a','b','c','d','e','f','g','z'] # Vertices
E = [('a','z'),('z','b'),('z','c'),('b','e'),('b','d'),('c','f'),('c','g'),
     ('g','f'),('e','d'),('g','f'),('d','a'),('g','a'),('e','f'),('b','c'),] # Edges

# # With I N P U T
# v = input("Masukkan vertex : ")
# V = re.split(",",v)
#
# E = []
# e =None
# while e != "sudah":
#     e = input("Masukkan edges : ")
#     c = re.split(",",e)
#     # c.append(int(c[2]))
#     if e != "sudah":
#         E.append(c)
#
# print(E,V)

# Mulai Membentuk Graph-nya
G = nx.Graph() # Empty Graph
for vertex in V: # Menambahkan semua vertexnya
    G.add_node(vertex)
for v1,v2 in E: # Menambahkan edgesnya
    if(v1 and v2 is not None):
        G.add_edge(v1,v2)
print('G: {0} nodes, {1} edges'.format(G.number_of_nodes(),G.number_of_edges()))

while True:
    pos = nx.spring_layout(G) # menentukan posisi node secara random
    # eL = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_nodes(G,pos) # membuat node graph
    nx.draw_networkx_labels(G,pos) # membuat weight graph
    # nx.draw_networkx_edge_labels(G,pos,edge_labels=eL) # memasang weight graph di edgenya
    nx.draw_networkx_edges(G,pos) # membuat edge graph
    plt.show() # menampilkan graph
    print("Rute terpendek")
    a= input("titik mulai : ")
    if(a == "sudah"):
        break
    b= input("titik akhir : ")
    print("Rute terpendek harusnya : ",nx.dijkstra_path(G,a,b))
    # print(nx.all_pairs_dijkstra_path(G,a,b))
    print(nx.all_shortest_paths(G,a,b))
    print(list(nx.dfs_edges(G,a)))
    print(list(nx.dfs_tree(G,a)))
    lol = list(nx.all_simple_paths(G,a,b))
    for i in range(len(lol)):
        print(lol[i],end="\n")
    plt.show()



while True:
    # eL = nx.get_edge_attributes(G,'weight')
    print("Rute terpendek")
    a= input("titik mulai : ")
    plt.close('all')
    if(a == "sudah"):
        break
    b= input("titik akhir : ")
    print("Rute terpendek harusnya : ",nx.dijkstra_path(G,a,b))
    # print(nx.all_pairs_dijkstra_path(G,a,b))
    print(nx.all_shortest_paths(G,a,b))
    print(list(nx.bfs_edges(G,a)))
    print(list(nx.bfs_tree(G,a)))
    lol = list(nx.all_simple_paths(G,a,b))
    for i in range(len(lol)):
        print(lol[i],end="\n")
    plt.show()
