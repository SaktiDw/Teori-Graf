from stuck import stuck
import networkx as nx
import pylab as plt

Matrix = stuck()
Matrix.V = ['a','b','c','d','e','f','g','z']
Matrix.default = [
    [0,0,0,1,0,0,1,1],
    [0,0,1,1,1,0,0,1],
    [0,1,0,0,0,1,1,1],
    [1,1,0,0,1,0,0,0],
    [0,1,0,1,0,1,0,0],
    [0,0,1,0,1,0,1,0],
    [1,0,1,0,0,1,0,0],
    [1,1,1,0,0,0,0,0]
]

Edges = stuck()
Edges.V = ['a','b','c','d','e','f','g','z']
Edges.default = [('a','z'),('z','b'),('z','c'),('b','e'),('b','d'),('c','f'),('c','g'),
     ('g','f'),('e','d'),('g','f'),('d','a'),('g','a'),('e','f'),('b','c'),] # Edges
G = nx.Graph()

def CreateMatrix():
    pass

def CreateVertexnEdges():
    pass

def dfs(E,source):
    return nx.dfs_tree(E,source)
    # print(nx.all_pairs_dijkstra_path(G,a,b))
    # print(nx.all_shortest_paths(G,a,b))
    print(list(nx.dfs_edges(G,a)))
    print(list(nx.dfs_tree(G,a)))
    # lol = list(nx.all_simple_paths(G,a,b))
    # for i in range(len(lol)):
    #     print(lol[i],end="\n")

def CreateEdges(V,E):
        if(type(E[0])) is list and E[0] != '': # matrix
            for i in range(len(V)):
                for j in range(len(E)):
                    if E[i][j] != 0:
                        edge = (V[i],V[j])
                        Edges.push(edge)
            E = Edges.items
        elif(type(E[0])) is tuple and E[0] != '':
            print("Anda menggunakan metode add Vertex & Edges ",end="\n")
            Edges.items = sorted(E)

def ShowGraph(V,E):
        if not E:
            print("Error! Harus input matrix atau edgenya")
        else:
             # Empty Graph
            for vertex in V: # Menambahkan semua vertexnya
                G.add_node(vertex)
            for v1,v2 in E: # Menambahkan edgesnya
                if(v1 and v2 is not None):
                    G.add_edge(v1,v2)

            pos = nx.spring_layout(G) # menentukan posisi node secara random
            # eL = nx.get_edge_attributes(G,'weight')
            nx.draw_networkx_nodes(G,pos) # membuat node graph
            nx.draw_networkx_labels(G,pos) # membuat weight graph
            # nx.draw_networkx_edge_labels(G,pos,edge_labels=eL) # memasang weight graph di edgenya
            nx.draw_networkx_edges(G,pos) # membuat edge graph
            plt.show() # menampilkan graph

def RuteTerpendek(G):
        print("Rute terpendek")
        a= input("titik mulai : ")
        b= input("titik akhir : ")
        print("Rute terpendek harusnya : ",nx.dijkstra_path(G,a,b))


while True:
    Input = input("1. Matrix \t 2. Vertex & Edges \t 3. Default Matrix \t 4. Default Edges \t 5. Show Graph \t 6. Rute Terpendek \t 7. Exit")
    if(Input == '1'):
        CreateMatrix()
    elif(Input == '2'):
        CreateVertexnEdges()
    elif(Input == '3'):
        CreateEdges(Matrix.V,Matrix.default)
    elif(Input == '4'):
        CreateEdges(Edges.V,Edges.default)
    elif(Input == '5'):
        ShowGraph(Edges.V,Edges.items)
    elif(Input == '6'):
        RuteTerpendek(G)
    elif(Input == '7'):
        print(Edges.items)
        exit()
    else:
        print("Wrong input")


