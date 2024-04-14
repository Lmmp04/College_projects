# I made this for a practical programming assignment on 4.13.2024, I learned the use of init and other methods inside of other classes. This will surely make my code more clear yet able to be complex.
from math import pi
from math import sqrt

class GeometricShape:
    def __init__(self, name):
        self.name = name

class Rectangle(GeometricShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_perimeter(self):
        return 2 * self.length + 2 * self.width
    def get_area(self): 
        return self.length * self.width

class Ellipse(GeometricShape):
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
    def get_perimeter(self):
        return pi * (3 * (self.semi_major_axis + self.semi_minor_axis))
    def get_area(self):
        return self.semi_major_axis * self.semi_minor_axis * pi
