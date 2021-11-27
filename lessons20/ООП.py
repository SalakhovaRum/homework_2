# # Создание функции классов
# def some_func():
#     return 2
#
# class SomeClass:
#     a = 1
#     def __init__(self,b,c,d):
#         self.b = b
#         self.c = c
#         self.d = d
#
# # Чтоб был какой-то метод,мы должна создать функцию:
#     def some_func(self):
#         return self.a
#     def some_func2(self):
#         return self.some_func()
#     def get_b(self):
#         return self.b
#     def get_c(self):
#         return self.c
#     def __str__(self):
#         return f`A: {self.a},b:{self.b}
# # self указывает на принадлежность к классам
#
# s = SomeClass(2,3,4)
# print (str(s))

# Конструктор - позволяет нам определить как будет создаваться обьект нашего класса(какие параметры, обрабатывать их всех
# функция: def __init__(self)
# Служебная функция- def __str__(self): возвращает строковое значение

# Абстрактный класс. Для этого испортируем библиотеку (from  abc import) и берем оттуда функцию abstractmethod
from abc import ABC,abstractmethod

class Animal(ABC):
    """Абстрактный класс животных"""

    # Означает что животное куда-то подвинулось
    def  move(self):
        print ('Im moving')
    def eat(self):
        print('Im eating')

    @abstractmethod
    def scream(self):
        raise Exception

class Cat(Animal):

    def __init__(self, height,width,name):
        self.name = name
        self. height = height
        self. width = width

    def scream(self):
        print (f'Meow my name is {self.name}')

    def sleep(self,hours):
        print(f'I will sleep for {hours} hours')



cat = Cat(10,18, 'Kitty')

cat.move()
cat.eat()
cat.scream()
cat.sleep(10)

# Приватный/Неприватный метод. Можем ли мы к ним обращаться через обьекты класса
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def scream(self):
        print(f'Gav me name is {self.name}')

    def _go_to_palka(self):
        print('I go to palka')

dog = Dog('Doggy')
dog.move()
dog.eat()
dog.scream()
dog._go_to_palka()

# Полиморфизм- свойство изменять поведение какого то метода налету.
#  В класс животных
# def attack(self):
#     print(f'{self.__.__name__} atacked some person')
# cat.atack
# dog.atack
#
# Хотим изменить поведение еды:
# def eating(food_name)
# print('Im eating {food name}')




