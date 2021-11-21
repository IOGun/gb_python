# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

persons_dict = {}
min_salary = 20000
all_salary = 0

with open("files/homework3.txt", "r") as hw3:
    content = hw3.readlines()

for person in content:
    person = person[:-1]
    persons_dict[person.split(" ")[0]] = int(person.split(" ")[1])

print(f"""
Список сотрудников с окладом менее {min_salary} рублей 
""")

for key in persons_dict:
    all_salary += persons_dict[key]
    if persons_dict[key] < min_salary:
        print(f"{key} {persons_dict[key]}")

print(f"""
Средняя зарплата сотрудников: {all_salary/len(content)}
""")