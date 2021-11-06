# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = input("Enter number: ")
maximum = 0

if num.isdigit():
    num = int(num)
    while num > 0:
        result = num % 10
        if result > maximum:
            maximum = result
        num = num // 10
    print(f"Max digit is {maximum}")
else:
    print("input error")
