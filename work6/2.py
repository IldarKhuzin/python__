# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного
# кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def get_total_weight (self, depth, weight_1sqm):
        total_weight = self._width * self._lenght * weight_1sqm * depth
        return total_weight

a = Road(5000, 20)

print(f'масса длины полотна равна {a.get_total_weight(5,25)/1000} тонн')
