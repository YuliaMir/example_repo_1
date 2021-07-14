class Dimensions:
    def __init__(self):
        self.dimensions = []

    def add_dimension(self, dimension):
        self.dimensions.append(dimension)

    def get_dimension(self, index):
        if index < len(self.dimensions):
            return self.dimensions[index]

        return 0

    def get_sorted(self):
        return sorted(self.dimensions)