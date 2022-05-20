from json.encoder import INFINITY
from queue_bfs import Queue
from vertex import Vertex

# initialise variables

vertex_names = ["r", "s", "t", "u", "v", "w", "x", "y"]
vertices = []
frontier = Queue()
adjacency_list_names = [
    ["s", "v"],
    ["r", "w"],
    ["u", "x", "w"],
    ["t", "x", "y"],
    ["r"],
    ["s", "t", "x"],
    ["w", "t", "u", "y"],
    ["u", "x"]
]
adjacency_list = [[], [], [], [], [], [], [], []]

# populate the vertices list with newly instantiated vertex objects
for name in vertex_names:
    if name == "s":
        index = vertex_names.index(name)
        colour = "grey"
        distance = 0
        parent = None
        vertex = Vertex(index, name, colour, distance, parent)
        vertices.append(vertex)
        frontier.enqueue(vertex)
    else:
        index = vertex_names.index(name)
        colour = "white"
        distance = float('inf')
        parent = None
        vertex = Vertex(index, name, colour, distance, parent)
        vertices.append(vertex)

# populate the adjacency list with vertex objects
for row in adjacency_list_names:
    for name in row:
        for vertex in vertices:
            if name == vertex.name:
                nested_row = adjacency_list[adjacency_list_names.index(row)].append(vertex)

# breadth first search until the 'frontier' list (undiscovered vertices) becomes empty
while frontier.is_empty() != True:
    current = frontier.dequeue()

    # discover vertices adjacent to the current vertex
    for vertex in adjacency_list[current.index]:
        if vertex.colour == "white":
            vertex.colour = "grey"
            vertex.distance = current.distance + 1
            vertex.parent = current
            frontier.enqueue(vertex)

    current.colour = "black"

# display each vertex's distance from the source vertex
for vertex in vertices:
    print(f"{vertex.name}'s distance is: {vertex.distance}")


