# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) != 4:
    print("Please enter 3 numbers")
else:
    for i, part in enumerate(argv[1:]):
        if part.isdigit():
            argv[i + 1] = int(part)
        else:
            print(f"Error: '{part}' is not digit")
            exit()

    print(f"Result: ({argv[1]} * {argv[2]}) + {argv[3]} = {(argv[1] * argv[2]) + argv[3]}")
