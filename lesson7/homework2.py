# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def quantity(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def quantity(self):
        return (self.v / 6.6) + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def quantity(self):
        return (self.h * 2) + 0.3

all_my_coats = [Coat(i) for i in range(1, 4)]
all_my_suits = [Suit(i) for i in range(1, 4)]

total = 0
for i, coat in enumerate(all_my_coats):
    print(f"Coat {i + 1}. V - {coat.v}, material - {coat.quantity}")
    total += coat.quantity

for i, suit in enumerate(all_my_suits):
    print(f"Suit {i + 1}. H - {suit.h}, material - {suit.quantity}")
    total += suit.quantity

print(f"Total: {total}")