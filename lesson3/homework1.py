# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def my_function(a, b):
    """
    Function a/b
    :param a: int
    :param b: int
    :return: float or error string
    """
    if b == 0:
        return f"Error (b is 0)"
    else:
        return float(a/b)

print("Function: a/b")

num_dict = {"a":0, "b":0}

for key in num_dict:
    i = input(f"Enter {key}: ")
    if i.isdigit():
        num_dict[key] = int(i)
    else:
        print(f"Input error '{i}' is not digit")
        break
else:
    print(f"Result of function a/b is {my_function(num_dict['a'], num_dict['b'])}")
