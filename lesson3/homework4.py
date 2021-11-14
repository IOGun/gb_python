# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_1(x, y):
    """
    x ** y
    :param x: float
    :param y: int <= 0
    :return: float
    """
    return x ** y

def my_func_2(x, y):
    """
    x ** y with cycle
    :param x: float
    :param y: int <=0
    :return: float
    """
    div = 1
    for i in range(abs(y)):
        div *= x
    return 1/div

def correct_num(x, y):
    """
    Return True if x and y is correct numbers, and False if it isn't that
    :param x: float
    :param y: int <= 0
    :return: Bool
    """
    if (x > 0) and (y <= 0):
        return True
    else:
        print("Error. Incorrect numbers")
        return False

my_dict = {"x":0.0, "y":0}

for key in my_dict:
    my_dict[key] = input(f"Enter number {key}: ")
else:
    if correct_num(float(my_dict["x"]), int(my_dict["y"])):
        print(f'1) Result of ** operation:    {my_func_1(float(my_dict["x"]), int(my_dict["y"]))}')
        print(f'1) Result of cycle operation: {my_func_2(float(my_dict["x"]), int(my_dict["y"]))}')
