import math


class Circle:
    def __init__(self, _radius):
        self.radius = _radius
    
    def get_area(self):
        return (math.pi * (self.radius ** 2))
    
    def __repr__(self):
        rep = 'Circle(radius: ' + str(self.radius) + ', area: ' + str(self.get_area()) + ')'
        return rep
    
    def __add__(self, other):
        return Circle((self.radius + other.radius))
    
    def __lt__(self, other):
        return self.radius < other.radius
        
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius

    def getRadius(self):
        return self.radius



circle = Circle(5)
circle2 = Circle(8)
print(repr(circle))
print(repr(circle+circle2))
print(circle < circle2)
print(circle > circle2)
print(circle == circle2)

c = Circle(7)
circles = [circle, circle2, c, circle + c, circle + circle2]

print(circles)
circles.sort()
print(circles)