# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

print("""
Standart list
""")


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
print([my_list[i] for i in range(1, len(my_list)) if my_list[i - 1] < my_list[i]])

print("""
Random list
""")

random_list = [randint(0, 300) for i in range(15)]
print(random_list)
print([random_list[i] for i in range(1, len(random_list)) if random_list[i - 1] < random_list[i]])



