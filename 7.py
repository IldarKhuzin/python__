# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

import math

class ComplexNumb:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'({self.a}+{self.b}j)'

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexNumb(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return ComplexNumb(new_a, new_b)


z1 = ComplexNumb(1, 2)
z2 = ComplexNumb(2, 3)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)
