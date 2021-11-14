# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[-1] + my_list[-2]


my_dict = {"a":0, "b":0, "c":0}

for key in my_dict:
    i = input(f"Enter number {key}: ")
    if i.isdigit():
        my_dict[key] = int(i)
    else:
        print(f"Error. '{i}' is not digit")
        break
else:
    result = my_func(my_dict["a"], my_dict["b"], my_dict["c"])
    print(f"Result is : {result}")