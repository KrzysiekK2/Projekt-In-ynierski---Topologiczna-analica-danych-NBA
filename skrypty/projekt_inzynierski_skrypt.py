import matplotlib.pyplot as plt
import gudhi

off_file = 'chtotal93.off'
point_cloud = gudhi.read_points_from_off_file(off_file=off_file)

rips_complex = gudhi.RipsComplex(points=point_cloud, max_edge_length=700)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=1)
diag = simplex_tree.persistence(min_persistence=2)

gudhi.plot_persistence_barcode(diag)
plt.show()

