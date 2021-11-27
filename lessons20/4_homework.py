from abc import ABC, abstractmethod


class Transport(ABC):

    def drive(self):
        print('Transport driving')

    def honk(self):
        print('Transport honking')

    def refill(self):
        print('Transport refilling')

    def traffic_accident(self):
        print(f'{self.__class__.__name__} traffic some person')

    # @abstractmethod
    # def scream(self):
    #     raise Exception


class Bicycle(Transport):

    def __init__(self, height, width, wheels):
        self.wheels = wheels
        self.height = height
        self.width = width

    def scream(self):
        print(f'How much {self.wheels} wheels')

    def speed(self, km):
        print(f'I will speed {km} km')


bicycle = Bicycle(10, 18, '4')

bicycle.drive()
bicycle.honk()
bicycle.refill()
bicycle.traffic_accident()
bicycle.scream()
bicycle.speed(5)


class MotoTransport(Transport):

    def __init__(self, height, width, winter):
        self.winter = winter
        self.height = height
        self.width = width

    def noise(self):
        print(f'Very mush {self.noise} ')

    def speed(self, km):
        print(f'I will speed {km} km')


motoTransport = MotoTransport(20, 25, 'no')

motoTransport.drive()
motoTransport.honk()
motoTransport.refill()
motoTransport.traffic_accident()
motoTransport.speed(30)
motoTransport.noise()


class Car(Transport):

    def __init__(self, height, width, passengers ):
        self.passengers = passengers
        self.height = height
        self.width = width

    def passengers(self):
        print(f'Very mush {self.passengers} we can not risk moving')

    def speed(self, km):
        print(f'I will speed {km} km')

car = Car(20, 25, 8)

car.drive()
car.honk()
car.refill()
car.traffic_accident()
car.speed(35)


class Minibuses(Transport):

    def __init__(self, height,width,name):
        self.name = name
        self. height = height
        self. width = width

    def charging(self,hours):
        print(f'I will charging for {hours} hours')

    def name(self):
        print(f'My {self.name} name is Trollybus')

    def speed(self, km):
        print(f'I will speed {km} km')

    def _go_to_passangens(self):
        print('I go to passangens')

minibuses = Minibuses(100, 155, 'Ляля')

minibuses.drive()
minibuses.honk()
minibuses.refill()
minibuses.traffic_accident()
minibuses.speed(20)
minibuses.charging(15)
minibuses._go_to_passangens()



