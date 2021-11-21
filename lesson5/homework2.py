# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("files/homework2.txt", "r") as hw2:
    content = hw2.readlines()

print(f"Количество строк в файле {hw2.name}: {len(content)}")

for i, f_string in enumerate(content):
    print(f"Количество слов в {i + 1}-ой строке: {len(f_string.split(' '))}")
