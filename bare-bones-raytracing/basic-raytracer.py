# import standard libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# import custom functions
import import_mesh
import visualize_mesh

# import mesh file
filename = 'meshes/edge-vertice-cube.txt'
vertices, edges = import_mesh.read_mesh_from_file(filename)

# display mesh
visualize_mesh.display_mesh(vertices, edges)
