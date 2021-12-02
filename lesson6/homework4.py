# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name,  is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            return True
        else:
            return False

    def stop(self):
        if self.speed == 0:
            return True
        else:
            return False

    def turn(self, direction = "forward"):
        print(direction)

    def show_speed(self):
        print(f"Скорость: {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость: {self.speed} - Превышение скорости")
        else:
            print(f"Скорость: {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость: {self.speed} - Превышение скорости")
        else:
            print(f"Скорость: {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True




speed = 100
color = "red"
name = "BMW"
is_police = False

sport_car = SportCar(speed, color, name, is_police)
work_car = WorkCar(speed, color, name, is_police)
town_car = TownCar(speed, color, name, is_police)
police_car = PoliceCar(speed, color, name, is_police)

#-----------------------------------SportCar---------------------------------------------------------------------------

print(f""" -----------------------------------------------------------------------------------------------------------
Sport Car

Speed: {sport_car.speed}, 
Color: {sport_car.color},
Name: {sport_car.name}
Is_police: {sport_car.is_police}
""")

if sport_car.go():
    print("Машина находится в движении")
else:
    print("Машина стоит")

if sport_car.stop():
    print("Машина стоит")
else:
    print("Машина находится в движении")

sport_car.turn()
sport_car.show_speed()

#-----------------------------------WorkCar----------------------------------------------------------------------------

print(f""" -----------------------------------------------------------------------------------------------------------
Work Car

Speed: {work_car.speed}, 
Color: {work_car.color},
Name: {work_car.name}
Is_police: {work_car.is_police}
""")

if work_car.go():
    print("Машина находится в движении")
else:
    print("Машина стоит")

if work_car.stop():
    print("Машина стоит")
else:
    print("Машина находится в движении")

work_car.turn('left')
work_car.show_speed()

#-----------------------------------TownCar----------------------------------------------------------------------------

print(f""" -----------------------------------------------------------------------------------------------------------
Town Car

Speed: {town_car.speed}, 
Color: {town_car.color},
Name: {town_car.name}
Is_police: {town_car.is_police}
""")

if town_car.go():
    print("Машина находится в движении")
else:
    print("Машина стоит")

if town_car.stop():
    print("Машина стоит")
else:
    print("Машина находится в движении")

town_car.turn('left')
town_car.show_speed()

#-----------------------------------PoliceCar---------------------------------------------------------------------------

print(f""" -----------------------------------------------------------------------------------------------------------
Police Car

Speed: {police_car.speed}, 
Color: {police_car.color},
Name: {police_car.name}
Is_police: {police_car.is_police}
""")

if police_car.go():
    print("Машина находится в движении")
else:
    print("Машина стоит")

if police_car.stop():
    print("Машина стоит")
else:
    print("Машина находится в движении")

police_car.turn('right')
police_car.show_speed()
