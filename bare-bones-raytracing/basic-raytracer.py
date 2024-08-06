# import standard libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# import custom functions
import import_mesh
import visualize_mesh

# import simple cube mesh
filename = 'meshes/edge-vertice-cube.txt'
vertices, edges = import_mesh.read_simple_mesh(filename)
# display simple mesh
visualize_mesh.display_mesh(vertices, edges)

# import trianglur cube mesh
filename_triangle = 'meshes/triangle-cube.txt'
vertices, edges, triangles = import_mesh.read_triangle_mesh(filename_triangle)
visualize_mesh.display_triangle_mesh(vertices, edges, triangles)