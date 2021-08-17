from lib import Node, Graph
from definitions import OUTPUT_DIR

print(OUTPUT_DIR)

a = Node({"name": "A"})
b = Node({"name": "B"})
c = Node({"name": "C"})
d = Node({"name": "D"})
e = Node({"name": "E"})
f = Node({"name": "F"})
g = Node({"name": "G"})
h = Node({"name": "H"})
i = Node({"name": "I"})
j = Node({"name": "J"})
k = Node({"name": "K"})
l = Node({"name": "L"})
m = Node({"name": "M"})
n = Node({"name": "N"})

G = Graph(a.add_sons([
    b.add_sons([h.add_sons([j]), i]),
    d.add_sons([g.add_sons([k])]),
    c.add_sons([e.add_sons([l,m]), f.add_sons([n])])
]))

def init():
    source_node = input("Source node: ")
    to_search   = input("Node to search: ")
    while(True):
        algorithm = input("Algorithm (dfs or bfs): ")
        if algorithm.upper() in ("BFS", "DFS"):
            break
    return source_node, to_search, algorithm

if __name__ == "__main__":
    G.display('graph.html')
    source_node, to_search, algorithm = init()

    value, counter = G.search_node(source_node, to_search, algorithm)

    if counter == 0:
        print(f"Le noeud {source_node} n'existe pas dans le graph.")
    elif value is None:
        print("Node not found!")
    else:
        print(f"Le noeud {to_search} est trouve apres avoir visite {counter} noeuds")