# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

num = input("Enter number of second: ")

if num.isdigit():
    num = int(num)

    hour = num // 3600
    minute = (num - (hour * 3600)) // 60
    sec = num % 60
    print(f"{hour:02}:{minute:02}:{sec:02}")
else:
    print("input error")
