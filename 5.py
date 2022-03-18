# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).


class Store:

    def __init__(self):
        self.store = {}

    def fill_store (self, store):
        for key, value in store.items():
            if key in self.store:
                self.store[key] += value
            else:
                self.store[key] = value
        print(f'сейчас на складе {self.store}')

    def del_store(self, store):
        for key, value in store.items():
            if key in self.store:
                self.store[key] += value
            else:
                self.store[key] = value
        print(f'сейчас на складе {self.store}')

class Equipment:

    def __init__(self, weight, voltage):
        self.weight = weight
        self.voltage = voltage

    def __str__(self):
        return f'{self.weight} кг и рабочее напряжение {self.voltage} - '

    def __repr__(self):
        return f'{self.weight} кг и рабочее напряжение {self.voltage} - '


class Printer(Equipment):
    def __init__(self, print_speed):
        self.print_speed = print_speed

class Scanner(Equipment):
    def __init__(self, scan_speed):
        self.scan_speed = scan_speed

class Xerox(Equipment):
    def __init__(self, copy_speed):
        self.copy_speed = copy_speed

first_equip = Equipment(4, 220)
sec_equip = Equipment(3,127)
third_equip = Equipment(5,220)

my_store = {
    first_equip: 4,
    sec_equip: 5,
    third_equip: 8
}

store = Store()
store.fill_store(my_store)
store.fill_store({first_equip: 6})
store.del_store({sec_equip: 3})
store.del_store({third_equip: 1})
