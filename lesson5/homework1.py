# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

hw_in = []

while True:
    my_string = input("Enter string: ")
    if my_string == '':
        break
    else:
        my_string = my_string + '\n'
        hw_in.append(my_string)


with open("temp/homework1.txt", "w") as hw1:
    hw1.writelines(hw_in)