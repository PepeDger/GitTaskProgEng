from abc import ABC
import math


class AbstractFigure(ABC):
    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

    def area_bigger_than_other(self, other: 'AbstractFigure'):
        return self.area() > other.area()

    def perimeter_bigger_than_other(self, other: 'AbstractFigure'):
        return self.perimeter() > other.perimeter()


class Square(AbstractFigure):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Неадекватное значение стороны")
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return self.side * 4


class Rectangle(AbstractFigure):
    def __init__(self, length: float, width: float):
        if width <= 0 or length <= 0:
            raise ValueError("Неадекватное значение одной из сторон")
        self.width = width
        self.length = length

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Triangle(AbstractFigure):
    def __init__(self, side1: float, side2: float, side3: float):
        if not self.is_valid_triangle(side1, side2, side3):
            raise ValueError("Неадекватные стороны треугольника")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        return ((a + b > c) and (a + c > b) and
                (b + c > a) and all(x > 0 for x in [a, b, c]))

    def area(self) -> float:
        # Формула Герона
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) *
                         (s - self.side2) * (s - self.side3))

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3


class Circle(AbstractFigure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    print(Circle(3).area_bigger_than_other(Square(10)))
    print(Circle(10).area())

