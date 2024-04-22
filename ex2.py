import matplotlib.pyplot as plt
import gudhi
import numpy as np

point_cloud = np.array([[2., 6.], [4., 6.], [6., 3.], [4., 0.], [2., 0.], [0., 3.]])

rips_complex = gudhi.RipsComplex(points=point_cloud, max_edge_length=7)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=3)
diag = simplex_tree.persistence(min_persistence=0.4)

gudhi.plot_persistence_barcode(diag)
plt.show()