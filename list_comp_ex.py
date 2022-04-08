from cmath import sqrt


my_string = "Cane Cagnaccio matita controller gatto"
words = my_string.split()
new_word_list = []
for word in words:
    if len(word) <= 5:
        new_word_list.append(word)
print(new_word_list)

new_word_list = [word for word in my_string.split() if len(word) <= 5]
print(new_word_list)

#upper_case_vowels = [char for char in my_string.upper() if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U']
upper_case_vowels = [char for char in my_string.upper() if char in 'AEIOU']
print(upper_case_vowels)


def my_sum(*args):
    return sum(args)


print(my_sum(1,3,4,7,9))

class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z
    # @property
    # def x(self):
    #     return self.x
    # @x.setter
    # def x(self, value):
    #     self.x = value
    # @property
    # def y(self):
    #     return self.y
    # @y.setter
    # def y(self, value):
    #     self.y = value
    # @property
    # def z(self):
    #     return self.z
    # @z.setter
    # def z(self, value):
    #     self.z = value
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    # def __pitagora(self):
    #     return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)
    
    def __eq__(self, other):
        return Vector(self.x == other.x, self.y == other.y, self.z == other.z)

    def __repr__(self):
        rep = 'Vector(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
        return rep

v = Vector(2, 3, 6)
print(v + Vector(3, 4, 5))
print(v * Vector(3, 4, 5))
print(v == Vector(3, 4, 5))
print(repr(v))