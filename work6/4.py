# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_polis = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = is_polis

    def go(self):
        return 'машина едет'

    def stop(self):
        return 'машина стоит'

    def turn(self, direction):
        return f'машина повернула на{direction}'

    def show_speed(self):
        return f'ваша скорость {self.speed}'

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return 'вы превышаете скорость'
        else:
            return 'нормальная скорость'

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return 'вы превышаете скорость'
        else:
            return 'нормальная скорость'

class SportCar(Car):
    pass

class PolisCar(Car):
    pass

town_car = TownCar(70, 'red', 'Volga', False)
print(town_car.speed, town_car.name, town_car.color)

work_car = WorkCar(30, 'blue', 'Belarus', False)
print(work_car.name, work_car.speed, work_car.color)

sport_car = SportCar(150,'yellow', 'Porshe', False)
print(sport_car.color, sport_car.name, sport_car.is_polis)

polis_car = PolisCar(100, 'white', 'VAZ', True)
print(polis_car.is_polis, polis_car. name, polis_car.speed)

print(town_car.show_speed())
print(work_car.show_speed())
print(sport_car.show_speed())
