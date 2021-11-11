# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

while True:
    num = input("Enter number of month [1..12]: ")
    if num.isdigit():
        num = int(num)
        if num < 1 or num > 12:
            print(f"Error month {num} is not exist")
            print("Please try again")
        else:
            break
    else:
        print(f"Error {num} is not digit")
        print("Please try again")

print(num)

season_list = ["winter/зима", "winter/зима", "spring/весна", "spring/весна", "spring/весна", "summer/лето",
               "summer/лето", "summer/лето", "autumn/осень",  "autumn/осень", "autumn/осень", "winter/зима"]

season_dict = {1:"winter/зима", 2:"winter/зима", 3:"spring/весна", 4:"spring/весна", 5:"spring/весна", 6:"summer/лето",
             7:"summer/лето", 8:"summer/лето", 9:"autumn/осень", 10:"autumn/осень", 11:"autumn/осень", 12:"winter/зима"}

print(f"Dict of seasons. Month {num} is {season_dict[num]}")
print(f"List of seasons. Month {num} is {season_list[num-1]}")

