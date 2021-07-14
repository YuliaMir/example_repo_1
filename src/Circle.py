from src.Figure import Figure
import math


class Circle(Figure):

    def get_name(self):
        return 'Circle'

    def _calculate_area(self):
        return math.pi * self.dimensions.get_dimension(0) ** 2

    def _calculate_perimeter(self):
        return 2 * (self.dimensions.get_dimension(0) * math.pi)
