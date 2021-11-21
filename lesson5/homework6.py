# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def to_int(str):
    i = ""
    for ch in str:
        if not ch.isdigit():
            break
        else:
            i += ch
    return int(i)


def to_separate(my_str):
    sum =0
    tmp = my_str.split()
    name = tmp[0]
    for i in tmp[1:]:
        if i == "—":
            continue
        else:
            sum += to_int(i)
    return name, sum

hw6_dict = {}

with open("files/homework6.txt", "r") as hw6:
    content = hw6.readlines()

print(content)
for my_line in content:
   name, sum = to_separate(my_line)
   hw6_dict[name] = sum

print(hw6_dict)