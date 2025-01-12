import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

n = int(input('Введите радиус: '))

if n > 0:
    circle = Circle(n)
    print(f'Ваш радиус: {circle.get_radius()}')
else:
    print('Радиус не может быть отрицательным.')

a = int(input('Введите новый радиус: '))
if a > 0:
    circle = Circle(a)
    print(f'Ваш радиус: {circle.get_radius()}')
else:
    print('Радиус не может быть отрицательным.')