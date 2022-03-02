# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен
# выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'запуск отрисовки'

class Pen(Stationery):

    def draw(self):
        return f'запуск отрисовки {self.title}'

class Pensil(Stationery):

    def draw(self):
        return f'запуск отрисовки {self.title}'

class Handle(Stationery):

    def draw(self):
        return f'запуск отрисовки {self.title}'

pen = Pen('ручкой')
print(pen.draw())

pensil = Pensil('карандашом')
print(pensil.draw())

handle = Handle('фломастером')
print(handle.draw())