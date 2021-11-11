# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_for_test = []
i = 0

while True:
    text = f"""Please enter element № {i} 
(enter 'exit' or 'stop' for exit): """
    element = input(text)

    if (element == "exit") or (element == "stop"):
        break
    list_for_test.append(element)
    i += 1

print(f"""
There are {len(list_for_test)} elements in list""")
print(f"Previos:   {list_for_test}")

if len(list_for_test) % 2 != 0:                                 # Нечетное
    for i in range(0, len(list_for_test)-1, 2):
        list_for_test[i], list_for_test[i + 1] = list_for_test[i + 1], list_for_test[i]
else:                                                           # Четное
    for i in range(0, len(list_for_test), 2):
        list_for_test[i], list_for_test[i + 1] = list_for_test[i + 1], list_for_test[i]

print(f"Now:       {list_for_test}")
