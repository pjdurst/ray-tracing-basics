# This file contains several different methods of plotting a mesh.

# import standard libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection, Poly3DCollection


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


# display a more complicated mesh made up of edges, vertices, and triangles
# each face of the cube is made up of two triangles
# several variables go into Poly3DCollection that we will cover in later examples
def display_triangle_mesh(vertices, edges, triangles):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    edge_lines = []
    for edge in edges:
        point1 = vertices[edge[0]]
        point2 = vertices[edge[1]]
        edge_lines.append([point1, point2])

    edge_collection = Line3DCollection(edge_lines, colors='k', linewidths=2)
    ax.add_collection3d(edge_collection)

    face_polygons = []
    for triangle in triangles:
        poly = [vertices[triangle[0]], vertices[triangle[1]], vertices[triangle[2]]]
        face_polygons.append(poly)

    face_collection = Poly3DCollection(face_polygons, color='cyan', alpha=0.5)
    ax.add_collection3d(face_collection)

    # Set limits
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

    # Label the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()