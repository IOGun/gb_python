# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    __weight = 25
    __tickness = 5

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def total(self):
        return self.__weight * self.__tickness * self._lenght * self._width

my_road = Road(5000, 20)
print(f"For road with lenght {my_road._lenght} m. and width {my_road._width} m. needs {my_road.total() / 1000} ton")