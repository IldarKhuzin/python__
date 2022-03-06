# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора
# @property.

from abc import ABC, abstractmethod

class Cloth(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Cloth):

    def __init__(self,v):
        self.v = v

    @property
    def consumption(self):
        return self.v/6.5 +0.5

class Suit(Cloth):

    def __init__(self,h):
        self.h = h

    @property
    def consumption(self):
        return self.h*2 + 0.3

def get_sum(suit, coat):
    return suit + coat


s = Suit(5)
print(s.consumption)
c = Coat(6)
print(c.consumption)
print(get_sum(s.consumption,c.consumption))
