from abc import ABC

class Geometric(ABC):
    '''Абстрактный класс геометрических фигур'''
    def draw(self):#(рисовать)
        print('I am drawing')
    def plot(self): #чертить
        print ('I an ploting')


class triangles(Geometric)
    def __init__(self, size, perimeter, square ):
        self.size = size
        self.perimeter = perimeter
        self.square = square

    a = int(input())
    b = int(input())
    c = int(input())
    perimeter  = (a + b + c) / 2
    square = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def corners(self):
        print('there are 3 corners')

    def vertexes(self):
        print('there are 3 vertices')

triangles = triangles(4,5,10)
triangles.perimeter()
triangles.square()
triangles.size()
triangles.a()
triangles.c()
triangles.b()
triangles.draw()
triangles.plot()

print()


class quadrate(Geometrice)
    def __init__(self, size, perimeter, square ):
        self.size = size
        self.perimeter = perimeter
        self.square = square


    def corners(self):
        print('there are 4 corners')

    def vertexes(self):
        print('there are 4 vertices')

    a = int(input("Введите сторону квадрата(целые числа): "))

    print("S =", a * a)

    a = float(input("Введите сторону квадрата(вещественные числа): "))

    print("P =", a * 4)
quadrate = quadrate(10,5,20)
quadrate.size()
quadrate.perimeter()
quadrate.square()
quadrate.a()
quadrate.draw()
quadrate.plot()

print()


class circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    @staticmethod
    def staticmethod():
        print('static method called')

circle = circle(10)
circle.perimeter()
circle.area()
circle.staticmethod()
circle.draw()
circle.plot()


class rectangle(Geometric)
    def __init__(self, size, perimeter, square ):
        self.size = size
        self.perimeter = perimeter
        self.square = square

    sideA = int(input("Длина: "))
    sideB = int(input("Ширина: "))

    area = sideA * sideB;

    print("Площадь прямоугольника: ", area)

    sideA = int(input("Длина: "))
    sideB = int(input("Ширина: "))

    perimeter = (sideA + sideB) * 2;

    print("Периметр прямоугольника: ", perimeter)

    def corners(self):
        print('there are 4 corners')

    def vertexes(self):
        print('there are 4 vertices')

    def diagonal(self):
        print('there are 2 diagonal')

rectangle = rectangle(10,20,50)
rectangle.perimeter()
rectangle.size()
rectangle.square()
rectangle.plot()
rectangle.draw()