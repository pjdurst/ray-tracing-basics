# This file contains several different methods of importing and storing a mesh.


# function to import a mesh made up of edges and vertices
def read_simple_mesh(filename):
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

# function to import a mesh made up of edges, vertices, and triangles
def read_triangle_mesh(filename):
    vertices = []
    edges = []
    triangles = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        reading_vertices = False
        reading_edges = False
        reading_triangles = False

        for line in lines:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            if 'Vertices:' in line:
                reading_vertices = True
                reading_edges = False
                reading_triangles = False
                continue
            if 'Edges:' in line:
                reading_vertices = False
                reading_edges = True
                reading_triangles = False
                continue
            if 'Triangles:' in line:
                reading_vertices = False
                reading_edges = False
                reading_triangles = True
                continue
            if reading_vertices:
                vertex = tuple(map(float, line[1:-1].split(',')))
                vertices.append(vertex)
            if reading_edges:
                edge = tuple(map(int, line[1:-1].split(',')))
                edges.append(edge)
            if reading_triangles:
                triangle = tuple(map(int, line[1:-1].split(',')))
                triangles.append(triangle)

    return vertices, edges, triangles