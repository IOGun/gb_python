# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_ful_name(self):
        print(f"Full name of {self.position}: {self.surname} {self.name}")

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        print(f"Total for {self.name}: {total_income}")

name = "Ivan"
surname = "Ivanov"
position = "CEO"
wage = 10000
bonus = 1001

ceo = Position(name, surname, position, wage, bonus)

ceo.get_total_income()
ceo.get_ful_name()

print(ceo.name)
print(ceo.surname)
print(ceo.position)
print(ceo._income)