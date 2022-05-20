class Vertex():
    def __init__(self, index, name, colour, distance, parent):
        self.index = index
        self.name = name
        self.colour = colour
        self.distance = distance
        self.parent = parent

    def __repr__(self):
        return f"name: {self.name}"
    