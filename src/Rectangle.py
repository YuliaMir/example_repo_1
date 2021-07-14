from src.Figure import Figure


class Rectangle(Figure):

    def get_name(self):
        return 'Rectangle'

    def _calculate_area(self):
        return self.dimensions.get_dimension(0) * self.dimensions.get_dimension(1)

    def _calculate_perimeter(self):
        return 2 * (self.dimensions.get_dimension(0) + self.dimensions.get_dimension(1))

