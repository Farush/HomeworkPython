import time

# 1. Создать класс TrafficLight (светофор).
class TrafficLight:
    __color = ''

    def running(self):
        i = 0
        while i < 1: # we can thınk of a dıfferent cycle breaking method, time referenced for instance
            __color = 'red'
            print(f'Color is {__color}')
            time.sleep(7)
            __color = 'yellow'
            print(f'Color is {__color}')
            time.sleep(3)
            __color = 'green'
            print(f'Color is {__color}')
            time.sleep(7)
            i += 1

tr = TrafficLight()
tr.running()


# 2. Реализовать класс Road (дорога).
class Road:
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width

    def mass(self, density, thickness):
        self.dens = density  # this could be a constant
        self.thick = thickness
        return f'{self.length * self.width * self.dens * self.thick / 1000}т.'


bakerStreet = Road(5000, 20)
print(bakerStreet.mass(25, 5))


# 3. Реализовать базовый класс Worker (работник).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income



class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


person1 = Position('Ivanov', 'Ivan', 'engineer', {'wage': 45000, 'bonus': 20000})
person2 = Position('Petrov', 'Egor', 'manager', {'wage': 38000, 'bonus': 15000})

print(person1.get_full_name())
print(person1.get_total_income())

print(person2.get_full_name())
print(person2.get_total_income())

# 4. Реализуйте базовый класс Car.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The car {self.name} goes')

    def stop(self):
        print(f'The car {self.name} stopped')

    def turn(self, direction):
        if direction == 1 or direction is True or direction == 'right':
            print(f'The car {self.name} turned right')
        elif direction == 0 or direction is False or direction == 'left':
            print(f'The car {self.name} turned left')
        else:
            print(f'Машина {self.name} повернула не туда. Укажите верное направление')

    def show_speed(self):
        print(f"The {self.name} car's speed is {self.speed}")


car1 = Car(100, 'blue', 'UAZ', True)
car1.go()
car1.stop()
car1.turn('dfgsadgr')
car1.show_speed()
print(car1.is_police)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'The speed {self.speed} is to high. Must not be more than 60 km/h')
        else:
            print(f'The speed is {self.speed} km/h')


car2 = TownCar(100, 'blue', 'NIVA', True)  # ıs_polıce должен переопределиться как False
car2.go()
car2.stop()
car2.turn(1)
car2.show_speed()
print(car2.is_police)


class SportCar(Car):

    def __init__(self, speed, color, name, gear, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.gear = gear

    def show_gear(self):
        print(f'{self.name} is at {self.gear}th gear')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'The speed {self.speed} is to high. Must not be more than 60 km/h')
        else:
            print(f'The speed is {self.speed} km/h')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=False, is_patroling=False):
        super().__init__(speed, color, name, is_police)
        self.is_patroling = is_patroling
        self.is_police = True


car3 = PoliceCar(100, 'black', 'Ford')
car3.turn(0)
print(car3.is_police)
car4 = WorkCar(40, 'grey', 'Ford')
car4.show_speed()
car5 = SportCar(200, 'red', 'Ferrari', 5)
print(car5.gear)
car5.show_gear()

# 5. Реализовать класс Stationery (канцелярская принадлежность).

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')

class Handle(Stationary):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

pen = Pen('Parker')
pen.draw()

pencil = Pencil('Koh-i-Noor')
pencil.draw()

marker = Handle('NoName')
marker.draw()
