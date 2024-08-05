import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def read_mesh_from_file(filename):
    vertices = []
    edges = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        reading_vertices = False
        reading_edges = False

        for line in lines:
            if 'Vertices:' in line:
                reading_vertices = True
                reading_edges = False
                continue
            if 'Edges:' in line:
                reading_vertices = False
                reading_edges = True
                continue
            if reading_vertices:
                vertex = tuple(map(float, line.strip()[1:-1].split(',')))
                vertices.append(vertex)
            if reading_edges:
                edge = tuple(map(int, line.strip()[1:-1].split(',')))
                edges.append(edge)

    return vertices, edges

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

# Usage
filename = 'edge-vertice-cube.txt'
vertices, edges = read_mesh_from_file(filename)
display_mesh(vertices, edges)
