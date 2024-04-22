import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_edge(1, 4)
g.add_edge(1, 6)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 2)


pos = {1:(2, 6), 2:(4, 6), 3:(6, 3), 4:(4, 0), 5:(2, 0), 6:(0, 3)}
nx.draw(g, pos, with_labels=True, node_size=800)
plt.show()