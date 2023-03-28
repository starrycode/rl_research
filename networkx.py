import networkx as nx
G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3])

G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_node(H)

G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*

G.add_edges_from([(1, 2), (1, 3)])

G.add_edges_from(H.edges)

G.clear()

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

G.number_of_nodes()

G.number_of_edges()

DG = nx.DiGraph()
DG.add_edge(2, 1)   # adds the nodes in order 2, 1
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)
assert list(DG.successors(2)) == [1, 4]
assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)]

list(G.nodes)

list(G.edges)

list(G.adj[1])  # or list(G.neighbors(1))

G.degree[1]  # the number of edges incident to 1

G.edges([2, 'm'])

G.degree([2, 3])

G.remove_node(2)
G.remove_nodes_from("spam")
list(G.nodes)

G.remove_edge(1, 3)

G.add_edge(1, 2)
H = nx.DiGraph(G)  # create a DiGraph using the connections from G
list(H.edges())

edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)  # create a graph from an edge list
list(H.edges())

adjacency_dict = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
H = nx.Graph(adjacency_dict)  # create a Graph dict mapping nodes to nbrs
list(H.edges())