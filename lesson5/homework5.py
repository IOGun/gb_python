# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

sum = 0

with open("temp/homework5.txt", "w+") as hw5:
    hw5_line = [f"{randint(0, 10)} " for i in range(10) ]
    hw5.writelines(hw5_line)
    hw5.seek(0)
    my_line = hw5.readline()
    # print(my_line)
    for i in my_line[:-1].split(" "):
        sum += int(i)
    print(f"Сумма чисел {my_line}в файле {hw5.name} равна {sum}")