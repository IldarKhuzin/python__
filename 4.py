# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для
# каждого типа оргтехники.


class Store:
    def __init__(self):
        pass

class Equipment:
    def __init__(self, voltage, weight):
        self.voltage = voltage
        self.weight = weight

class Printer(Equipment):
    def __init__(self, print_speed):
        super().__init__(voltage=220, weight= self.weight)
        self.print_speed = print_speed

class Scanner(Equipment):
    def __init__(self, scan_speed):
        super().__init__(voltage= self.voltage, weight= 5)
        self.scan_speed = scan_speed

class Xerox(Equipment):
    def __init__(self, copy_speed):
        super().__init__(voltage= self.voltage, weight= self.weight)
        self.copy_speed = copy_speed
