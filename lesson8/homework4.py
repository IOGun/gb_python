# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class OfficeEquip:
    def __init__(self, name, model):
        self.name = name
        self.model = model

class Printer(OfficeEquip):
    def __init__(self, name, model, type, printing = True):
        super().__init__(name, model)
        self.type = type #laser, ink-jet
        self.printing = printing

class Scaner(OfficeEquip):
    def __init__(self, name, model, resolution, scaning = True):
        super().__init__(name, model)
        self.resolution = resolution # 600 dpi
        self.scaning = scaning

class Xerox(OfficeEquip):
    def __init__(self, name, model, speed ,copiring = True):
        super().__init__(name, model)
        self.speed = speed
        self.copiring = copiring

my_stor = Storage('Costco', 'NewYork')
my_printer = Printer('Canon', '1030', 'laser')
my_scaner = Scaner('HP', '8200', 4800,)
my_xerox = Xerox('Xerox', '6200', 100)

print(my_printer.model, my_scaner.model, my_xerox.model)

