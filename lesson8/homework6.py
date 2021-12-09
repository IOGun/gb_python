# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Storage:
    def __init__(self, name, address, equips):
        self.name = name
        self.address = address
        self.equips = equips

    def give_office_equip_to_user(self, equip):
        if self.equips.count(equip) > 0:
            self.equips.remove(equip)
            return equip
        else:
            return None

    def take_office_equip(self, equip):
        self.equips.append(equip)
        return equip

    def __str__(self):
        return f"{self.name} {self.address}"

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

class MyError(Exception):
    def __init__(self, text):
        self.text = text

my_printer = Printer('Canon', '1030', 'laser')
my_scaner = Scaner('HP', '8200', 4800,)
my_xerox = Xerox('Xerox', '6200', 100)

equips = [my_xerox, my_scaner, my_printer]
equips_to_store = []

for tmp in equips:
    while True:
        try:
            count_equip = input(f"Введите количество {tmp}, поступивших на склад: ")
            if not count_equip.isdigit():
                raise MyError("Ошибка ввода")
        except MyError as err:
            print(err)
            continue
        else:
            count_equip = int(count_equip)
            for i in range(count_equip):
                equips_to_store.append(tmp)
            break




my_stor = Storage('Costco', 'NewYork', equips_to_store)

print("---------------------------------------------------------------------------------------------")

print(f"На складе {my_stor}: {my_stor.equips}")

print("--------------------------------Взяли со склада----------------------------------------------")
print(my_stor.give_office_equip_to_user(my_printer))
print(f"На складе: {my_stor.equips}")

print("--------------------------------Вернули на склад---------------------------------------------")
print(my_stor.take_office_equip(my_printer))
print(f"На складе: {my_stor.equips}")