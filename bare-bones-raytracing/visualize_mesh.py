# This file contains several different methods of plotting a mesh.

# import standard libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# display a basic mesh made up of only edges and vertices
def display_mesh(vertices, edges):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    edge_lines = []
    for edge in edges:
        point1 = vertices[edge[0]]
        point2 = vertices[edge[1]]
        edge_lines.append([point1, point2])

    edge_collection = Line3DCollection(edge_lines, colors='k', linewidths=2)
    ax.add_collection3d(edge_collection)

    # Set limits
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

    # Label the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()