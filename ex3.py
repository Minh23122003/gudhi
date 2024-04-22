
import matplotlib.pyplot as plt
import gudhi
import numpy as np

with open('D:/3pcf_protein.pdb', 'r') as file:
    lines = file.readlines()

N_arr = []
O_arr = []

for line in lines:
    list = line.split()
    if list[0] == 'ATOM' and (list[2] == 'N' or list[2] == 'O'):
        x_coord = float(list[6])
        y_coord = float(list[7])
        z_coord = float(list[8])
        if list[2] == 'N':
            N_arr.append([x_coord, y_coord, z_coord])
        elif list[2] == 'O':
            O_arr.append([x_coord, y_coord, z_coord])
N_arr = np.array(N_arr)
O_arr = np.array(O_arr)

rips_complex = gudhi.RipsComplex(points=N_arr + O_arr, max_edge_length=10)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=10)
diag = simplex_tree.persistence(min_persistence=0.4)

gudhi.plot_persistence_barcode(diag)
plt.show()

# for l in lines:
#     print(l)