import igraph
import networkx
g = networkx.Graph()
g_ = igraph.Graph()
with open("countries.txt", "r") as f:
    for i in f.read().split("\n"):
        g.add_node(i)
        g_.add_vertex(i)
with open("all-roads.txt", "r") as f:
    for i in f.read().split("\n"):
        a, b, w = i.split()
        g.add_edge(a, b)
        g_.add_edge(a, b)
g.to_undirected()
print("|V|:", g.number_of_nodes())
print("|𝐸|:", g.number_of_edges())
print("Δ(G):", g_.maxdegree())
gg_ = igraph.Graph.subgraph(g_, g_.clusters()[0])
print("rad(G):", gg_.radius())
print("diam(G):", gg_.diameter())
a = []
for i in gg_.vs:
    if i.eccentricity() == gg_.radius():
        a.append(i)
print("center(G):", " ".join([i["name"] for i in a]))
l = 0
for i in gg_.cliques():
    if len(i) > l:
        l = len(i)
        a = i
print("clique Q:", " ".join(igraph.Graph.subgraph(gg_, a).vs["name"]))
print("stable set S:", " ".join(igraph.Graph.subgraph(gg_, gg_.largest_independent_vertex_sets()[0]).vs["name"]))
