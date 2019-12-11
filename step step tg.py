import networkx as nx # ini buat graph
import pylab as plt # ini supaya graphnya tampil
import collections # ini gak tau

# yield itu sama aja kyk return cuman bisa lebih banyak value
# continue itu kebalikan break

# ini buat cari semua rute dari source ke target
def all_simple_paths_graph(G, source, targets, cutoff):
    # ini buat nyimpan vertex yg udah di kunjungi
    visited = collections.OrderedDict.fromkeys([source])
    # print("visited ",dict(visited))
    stack = [iter(G[source])]
    # print("stack ",G[source])
    # print("lol",targets - visited.keys())
    while stack:
        children = stack[-1]
        # print("children",list(children))
        child = next(children, None)
        # print("child", list(children))
        if child is None:
            stack.pop()
            visited.popitem()
        elif len(visited) < cutoff:
            if child in visited:
                print(child,visited)
                continue
            if child in targets:
                yield list(visited) + [child]
            visited[child] = None
            if targets - visited.keys():  # expand stack until find all targets
                stack.append(iter(G[child]))
            else:
                visited.popitem()  # maybe other ways to child
        else:  # len(visited) == cutoff:
            for target in (set(targets) & (set(children) | {child})) - set(visited.keys()):
                yield list(visited) + [target]
            stack.pop()
            visited.popitem()

def partition(arr,low,high):
    i = ( low-1 )         # index element terkecil
    pivot = arr[high]     # pivot
    for j in range(low , high):
        # ini kalo element sekarang lebih kecil atau lebih besar dari pivot
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# ini buat simpan nama simpul
V = ['a','b','c','d','e','f','g','z']
# ini buat matrix
matrix = [
    [0,0,0,1,0,0,1,1],
    [0,0,1,1,1,0,0,1],
    [0,1,0,0,0,1,1,1],
    [1,1,0,0,1,0,0,0],
    [0,1,0,1,0,1,0,0],
    [0,0,1,0,1,0,1,0],
    [1,0,1,0,0,1,0,0],
    [1,1,1,0,0,0,0,0]
    ]

E = {} # menyimpan data vertex dan edges
for i in range(len(matrix)):
    edge = []
    for j in range(len(matrix)):
        if matrix[i][j] != 0:
            edge.append(V[j])
    E[str(V[i])] = (edge)
"""
{
'a': ['d', 'g', 'z'], 
'b': ['c', 'd', 'e', 'z'], 
'c': ['b', 'f', 'g', 'z'], 
'd': ['a', 'b', 'e'], 
'e': ['b', 'd', 'f'], 
'f': ['c', 'e', 'g'], 
'g': ['a', 'c', 'f'], 
'z': ['a', 'b', 'c']
}
"""

edges = [] #membuat list untuk kepenting menggambar graff
for i in range(len(V)):
    for j in range(len(matrix)):
        if matrix[i][j] != 0:
            edge = (V[i],V[j])
            edges.append(edge)
"""
[
    ('a', 'd'), ('a', 'g'), ('a', 'z'), ('b', 'c'), 
    ('b', 'd'), ('b', 'e'), ('b', 'z'), ('c', 'b'), 
    ('c', 'f'), ('c', 'g'), ('c', 'z'), ('d', 'a'), 
    ('d', 'b'), ('d', 'e'), ('e', 'b'), ('e', 'd'), 
    ('e', 'f'), ('f', 'c'), ('f', 'e'), ('f', 'g'), 
    ('g', 'a'), ('g', 'c'), ('g', 'f'), ('z', 'a'), 
    ('z', 'b'), ('z', 'c')
]
"""
G = nx.Graph() # Empty Graph
for vertex in V: # Menambahkan semua vertexnya
    G.add_node(vertex)
for v1,v2 in edges: # Menambahkan edgesnya
    if(v1 and v2 is not None):
        G.add_edge(v1,v2)

while True:
    # Ini masalah GUI graph
    pos = nx.spring_layout(G) # menentukan posisi node secara random
    nx.draw_networkx_nodes(G,pos) # membuat node graph
    nx.draw_networkx_labels(G,pos) # membuat label graph
    nx.draw_networkx_edges(G,pos) # membuat edge graph
    # plt.show() # menampilkan graph

    # ini masalah Input
    print("Welcome to Mobile Legends")
    print("Penting!!! Masukkan titik awal untuk mencari rute atau ketik \"sudah\" kalo udahan!\n")
    # perulangan buat mastikan inpu gk salah
    while True:
        a = input("titik awal: ")
        if a == "sudah":
            print("\nbye...bye..\n")
            exit()
        elif a not in V:
            print("Vertex yang anda maksud gk ada anjing!!")
        else:
            while True:
                b = input("titik akhir: ")
                if b not in V:
                    print("Vertex yang anda maksud gk ada anjing!!")
                else:
                    break
            break
    print("\nJadi ini adalah semua rute yang bisa anda laluli dari titik {} ke titik {}".format(a,b))
    rute = (list(all_simple_paths_graph(G,a,b,len(V))))

    jalur = [] # nyimpan jumlah panjang rute
    # perulangan buat ngambil panjang rute
    for i in range(len(rute)):
        jalur.append(len(rute[i]))
        print(rute[i])

    # sorting rute terpendek ke terpanjang
    quickSort(jalur,0,len(jalur)-1)

    print("\nDiantara semua jalur diatas, jalur terpendeknya adalah : ")
    #  tampilkan semua rute
    for j in range(len(rute)):
        if(len(rute[j])== jalur[0]):
            print (rute[j],end="\n")
    print()



