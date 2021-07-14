from src.Dimensions import Dimensions


class Figure:
    def __init__(self, dimensions: Dimensions):
        self.dimensions = dimensions

    def get_name(self):
        return 'Shape'

    def get_dimensions(self):
        return self.dimensions

    def _calculate_area(self):
        return 0

    def _calculate_perimeter(self):
        return 0

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Wrong class")
        return figure._calculate_area() + self._calculate_area()


