# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

text = "Enter number of string: "
i = input(text)
if i.isdigit():
    i = int(i)
    print(f"Number of string you can enter is {i}")
else:
    print("Error of enter. It is not digit. Number of string equal 1.")
    i = 1

while i:
    text = input('Enter string (print "end" for exit) : ')
    if text == "end":
        break
    number = input('Enter number (print "end" for exit): ')
    if number == "end":
        break

    print(f"Users text is '{text}', Users number is {number}")

    i -= 1

print("The End )))")
