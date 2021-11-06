# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = input("Enter number: ")

if num.isdigit():
    part1 = int(num)
    part2 = int(f"{num}{num}")
    part3 = int(f"{num}{num}{num}")
    result = part1 + part2 + part3
    print(f"{part1} + {part2} + {part3} = {result}")
else:
    print("input error")
