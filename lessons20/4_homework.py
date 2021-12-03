from abc import ABC


class Games(ABC):
    """Абстрактный класс игр"""

    def attack(self):
        print(f'{self.__class__.__name__} attack enemy')

    def block(self):
        print('blocked the hit')

    def kill(self):
        print(f'{self.__class__.__name__}')

    def death(self):
        print(f'{self.__class__.__name__} dead')

    # @abstractmethod
    #     def munder(self):
    #         pass


class Pubg_Mobile(Games):
    def __init__(self,lives ,level):
        self.lives = lives
        self.level = level
        self.name = 'Rumiya'

    def jump(self):
        print(f'jump and avoid hit')

    def die(self):
        print('dead')

    def punch(self):
        print('minus one life')


class Homescapes(Games):
    def __init__(self, level, endurance, name ):
        self.endurance = endurance
        self.level = level
        self.name = name


    def think(self):
        print('I think')

    def problems(self):
        print('Solve problems')

    def deceive(self):
        print('Deceive the main character')

    def murder(self, detalis):
            print(f'I will murder for {detalis}')


class Jetpack_Joyride(Games):
    def __init__(self, name, level,run ):
        self.name = name
        self.armor = level
        self.wisdom = run

    def turning(self):
        print('turn left')

    def jump_over(self):
        print('jump up')

    def strategy(self):
        print('build a stretegy')

    def murder(self, detalis):
        print(f'I will murder for {detalis}')

    def _shoot_an_arrow(self):
        """Это приватный метод"""
        print('I shoot an arrow')


class Car(Games):
    def __init__(self, speed, level):
        self.name = 'Bus'
        self.speed = speed
        self.rage = level

    def park(self):
        print('I am parkimg')

    def ride(self):
        print('I am riding ahead')

    def unwrap(self):
        print('I turn around on the spot')

    def murder(self, detalis):
        print(f'I will murder for {detalis}')

Pubg_Mobile = Pubg_Mobile(2,5)
Pubg_Mobile.jump()
Pubg_Mobile.die()
Pubg_Mobile.punch()
Pubg_Mobile.attack()
Pubg_Mobile.block()
Pubg_Mobile.kill()
Pubg_Mobile.death()

print()

Homescapes = Homescapes(5,'good','Olivia')
Homescapes.attack()
Homescapes.block()
Homescapes.kill()
Homescapes.death()
Homescapes.think()
Homescapes.problems()
Homescapes.deceive()
Homescapes.murder('Kirill')

print()

Jetpack_Joyride = Jetpack_Joyride('Kozel',5,10)
Jetpack_Joyride.murder(10)
Jetpack_Joyride.turning()
Jetpack_Joyride.jump_over()
Jetpack_Joyride.strategy()
Jetpack_Joyride._shoot_an_arrow()
Jetpack_Joyride.attack()
Jetpack_Joyride.block()
Jetpack_Joyride.kill()
Jetpack_Joyride.death()

print()

Car = Car(10,10)
Car.park()
Car.ride()
Car.unwrap()
Car.murder(10)
Car.death()
Car.death()
Car.kill()
Car.block()

print()

