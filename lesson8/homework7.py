# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, bi):
        self.a = a
        self.bi = bi

    def __add__(self, other):
        return ComplexNumber((self.a + other.a), (self.bi + other.bi))

    def __mul__(self, other):
        a = (self.a * other.a) - (self.bi * other.bi)
        bi = (self.bi * other.a) + (self.a * other.bi)
        return ComplexNumber(a, bi)

    def __str__(self):
        return f"{self.a} + ({self.bi})i"

c1 = ComplexNumber(2, 1)
c2 = ComplexNumber(3, 1)

c3 = c1 + c2
print(c3)

c3 = c1 * c2
print(c3)