from src.Dimensions import Dimensions
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle




triangle_dimensions = Dimensions()
triangle_dimensions.add_dimension(5)
triangle_dimensions.add_dimension(0)
triangle_dimensions.add_dimension(10)
triangle = Triangle(triangle_dimensions)
triangle.get_area()
triangle.get_perimeter()

rectangle_dimensions = Dimensions()
rectangle_dimensions.add_dimension(2)
rectangle_dimensions.add_dimension(3)
rectangle = Rectangle(rectangle_dimensions)
rectangle.get_area()
rectangle.get_perimeter()

square_dimensions = Dimensions()
square_dimensions.add_dimension(3)
square = Square(square_dimensions)
square.get_area()
square.get_perimeter()

circle_dimensions = Dimensions()
circle_dimensions.add_dimension(3)
circle = Circle(circle_dimensions)
circle.get_area()
circle.get_perimeter()



