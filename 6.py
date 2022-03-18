# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


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
        return f'{self.weight} кг и рабочее напряжение {self.voltage} вольт - '

    def __repr__(self):
        return f'{self.weight} кг и рабочее напряжение {self.voltage} вольт - '


class Printer(Equipment):
    def __init__(self,weight, voltage, print_speed):
        super(Printer, self).__init__(weight, voltage)
        self.print_speed = print_speed

class Scanner(Equipment):
    def __init__(self,weight, voltage, scan_speed):
        super(Scanner, self).__init__(weight, voltage)
        self.scan_speed = scan_speed
        try:
            if type(self.voltage) == int:
                pass
            else:
                print('введите корректно значение напряжения для сканера')
        except:
            pass


class Xerox(Equipment):
    def __init__(self,weight, voltage, copy_speed):
        super(Xerox, self).__init__(weight, voltage)
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
printer = Printer(1,127,3)
scanner = Scanner(3,'220volt',5)
xerox = Xerox(6,220, 2)
print(printer)
print(scanner)
print(xerox)
