from src.Figure import Figure
import math


class Triangle(Figure):

    def get_name(self):
        return 'Triangle'

    def _calculate_area(self):
        if not self._is_triangle():
            return None

        p = (self.dimensions.get_dimension(0) + self.dimensions.get_dimension(1) + self.dimensions.get_dimension(2))
        return math.sqrt(p * (p - self.dimensions.get_dimension(0)) * (p - self.dimensions.get_dimension(1)) * (p - self.dimensions.get_dimension(2)))

    def _calculate_perimeter(self):
        if not self._is_triangle():
            return None

        return self.dimensions.get_dimension(0) + self.dimensions.get_dimension(1) + self.dimensions.get_dimension(2)

    def _is_triangle(self):
        sides = self.dimensions.get_sorted()
        return sides[0] + sides[1] > sides[2]
