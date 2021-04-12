import igraph

g = igraph.Graph()
with open("countries.txt", "r") as f:
    for i in f.read().split("\n"):
        g.add_vertex(i)
with open("all-roads.txt", "r") as f:
    for i in f.read().split("\n"):
        a, b, w = i.split()
        g.add_edge(a, b, weight=int(w))
g.to_undirected()
print("|V|:", len(g.vs))
print()
print("|𝐸|:", len(g.es))
print()
print("Δ(G):", g.maxdegree())
print()
gg = igraph.Graph.subgraph(g, g.clusters()[0])
print("rad(G):", gg.radius())
print()
print("diam(G):", gg.diameter())
print()
a = []
for i in gg.vs:
    if i.eccentricity() == gg.radius():
        a.append(i)
print("center(G):", " ".join([i["name"] for i in a]))
print()
print("Maximum clique Q:", " ".join(igraph.Graph.subgraph(gg, gg.largest_cliques()[0]).vs["name"]))
print()
print("Maximum stable set S:", " ".join(igraph.Graph.subgraph(gg, gg.largest_independent_vertex_sets()[0]).vs["name"]))
print()
gq = gg.copy()
a = []
q = sorted([(i.source_vertex.degree() + i.target_vertex.degree(), i) for i in gg.es])
while len(q) != 0:
    n = q.pop(0)
    a.append((n[1].source_vertex["name"] + " - " + n[1].target_vertex["name"]))
    gq.delete_vertices([n[1].source, n[1].target])
    q = sorted([(i.source_vertex.degree() + i.target_vertex.degree(), i) for i in gq.es])
print("Maximum matching:\n" +





      '\n'.join(a))
print()
print("Minimum vertex cover R:", " ".join(
    [i for i in set(gg.vs["name"]) - set(igraph.Graph.subgraph(gg, gg.largest_independent_vertex_sets()[0]).vs["name"])]))
print()
print("Minimal spanning tree:")
r = gg.spanning_tree(gg.es["weight"])
print("\n".join(i.source_vertex["name"] + " - " + i.target_vertex["name"] for i in r.es))
print()
print(" ".join([gg.vs[i]["name"] for i in r.to_prufer()]))
print()