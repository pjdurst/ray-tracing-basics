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