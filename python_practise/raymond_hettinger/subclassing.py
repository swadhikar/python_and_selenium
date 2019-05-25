import math


class Circle(object):
    version = '0.1'

    def __init__(self, radius):
        self.diameter = 2 * radius

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2

    def area(self):
        p = self._perimeter()
        r = p / math.pi / 2
        return math.pi * (r ** 2)

    def perimeter(self):
        print('Perimeter ran from inside "Circle" class!')
        return math.pi * self.diameter

    _perimeter = perimeter


class Tire(Circle):
    ''' Tires are circles with corrected an odometer corrected perimeter '''

    def perimeter(self):
        print('Perimeter ran from inside "Tire" class!')
        return Circle.perimeter(self) * 1.25
