from src.Figure import Figure


class Square(Figure):

    def get_name(self):
        return 'Square'

    def _calculate_area(self):
        return self.dimensions.get_dimension(0) ** 2

    def _calculate_perimeter(self):
        return 4 * self.dimensions.get_dimension(0)

