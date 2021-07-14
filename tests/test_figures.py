import pytest

from src.Dimensions import Dimensions
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle


def test_no_zero_dimensions():
    right_triangle_dimensions = Dimensions()
    right_triangle_dimensions.add_dimension(4)
    right_triangle_dimensions.add_dimension(6)
    right_triangle_dimensions.add_dimension(10)
    triangle = Triangle(right_triangle_dimensions)
    dimensions = triangle.get_dimensions()

    assert dimensions.get_dimension(0) != 0, "Triangle should has 3 sides"
    assert dimensions.get_dimension(1) != 0, "Triangle should has 3 sides"
    assert dimensions.get_dimension(2) != 0, "Triangle should has 3 sides"

    broken_triangle_dimensions = Dimensions()
    broken_triangle_dimensions.add_dimension(4)
    triangle = Triangle(broken_triangle_dimensions)
    dimensions = triangle.get_dimensions()
    assert dimensions.get_dimension(1) == 0


test_no_zero_dimensions()


def test_rectangle_for_square():
    rectangle_dimensions = Dimensions()
    rectangle_dimensions.add_dimension(4)
    rectangle_dimensions.add_dimension(5)
    rectangle = Rectangle(rectangle_dimensions)
    dimensions = rectangle.get_dimensions()
    assert dimensions.get_dimension(0) != dimensions.get_dimension(1), "It's Square"

test_rectangle_for_square()

def test_circle_exist():
    circle_dimensions = Dimensions()
    circle_dimensions.add_dimension(1)
    circle = Circle(circle_dimensions)
    dimensions = circle.get_dimensions()
    assert dimensions.get_dimension(0) != 0, "Circle doesn't exist"

test_circle_exist()

def test_square_area_valid():
    square_dimensions = Dimensions()
    square_dimensions.add_dimension(2)
    square = Square(square_dimensions)
    dimensions = square.get_dimensions()
    assert dimensions.get_dimension(0) < 1, "Square area is more or equal 1"

test_square_area_valid()


