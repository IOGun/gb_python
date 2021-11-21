# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("files/homework4.txt", "r") as hw4:
    content = hw4.readlines()
    hw4_new_content = [f'{my_dict[hw4_string.split(" ")[0]]} {hw4_string.split(" ")[1]} {hw4_string.split(" ")[2]}' for hw4_string in content]

with open("temp/homework4.txt", "w") as hw4_new:
    hw4_new.writelines(hw4_new_content)
    print(f"Новый файл создан в папке: {hw4_new.name}")

