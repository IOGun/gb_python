# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


class Storage:
    def __init__(self, name, address, equips):
        self.name = name
        self.address = address
        self.equips = equips

    def give_office_equip(self, equip):
        if self.equips.count(equip) > 0:
            self.equips.remove(equip)
            return equip
        else:
            return None

    def take_office_equip(self, equip):
        self.equips.append(equip)

class OfficeEquip:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def __repr__(self):
        return f"{self.name} {self.model}"

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


my_printer = Printer('Canon', '1030', 'laser')
my_scaner = Scaner('HP', '8200', 4800,)
my_xerox = Xerox('Xerox', '6200', 100)

equips = [my_xerox, my_scaner, my_printer]

my_stor = Storage('Costco', 'NewYork', equips)


print(my_stor.equips)

print(my_stor.give_office_equip(my_printer))
print(my_stor.equips)

print(my_stor.take_office_equip(my_printer))
print(my_stor.equips)