from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius * self.__radius

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Square(Figure):
    def __init__(self, side):
        self.__side = side  # private attribute

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        p = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def perimeter(self):
        return self.__a + self.__b + self.__c


circle = Circle(3)
square = Square(4)
triangle = Triangle(3, 4, 5)


figures = [circle, square, triangle]

for figure in figures:
    print("Figure:", figure.__class__.__name__)
    print("Area:", round(figure.area(), 2))
    print("Perimeter:", round(figure.perimeter(), 2))
    print()