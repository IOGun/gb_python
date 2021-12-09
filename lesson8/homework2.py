# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
# с ошибкой.


class ZeroDiv(Exception):
    def __init__(self, text):
        self.text = text


my_num1 = int(input('Введите делимое: '))
try:
    my_num2 = int(input("Введите делитель: "))
    if my_num2 == 0:
        raise ZeroDiv("Ноль не может являться делителем")
except ZeroDiv as err:
    print(err)
else:
    print(f"Результат: {my_num1/my_num2}")

print("The End")