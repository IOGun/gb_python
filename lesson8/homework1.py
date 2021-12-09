# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    __d = 0
    __m = 0
    __y = 0
    def __init__(self, date):
        self.date = date
        Date.to_digit(self.date)

    @classmethod
    def to_digit(cls, date = None):

        if date:
            temp = date.split("-")
            __d = int(temp[0])
            __m = int(temp[1])
            __y = int(temp[2])
            print(__d, __m, __y)
            return Date.valid(__d, __m, __y)
        else:
            return None


    @staticmethod
    def valid(day, month, year):
        count = 0
        if day > 0 and day <= 31:
            print(f"Day {day} - OK")
            count +=1
        else:
            print(f"Day {day} - Error")

        if month > 0 and month <= 12:
            print(f"Month {month} - OK")
            count += 1
        else:
            print(f"Month {month} - Error")

        if year > 0:
            print(f"Year {year} - OK")
            count += 1
        else:
            print(f"Year {year} - Error")

        if count == 3:
            return [day, month, year]
        else:
            print('Date error')
            return None


Date.to_digit('12-01-2021')

print("""
-------------------------------------------------------------------------------------------------------
""")

Date.valid(33, 12, 2021)

print("""
-------------------------------------------------------------------------------------------------------
""")

date = Date('12-12-2021')
date.to_digit()

