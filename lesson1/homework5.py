# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете
# на одного сотрудника.

proceeds = float(input("Enter proceeds: "))  # выручка
spending = float(input("Enter spending: "))  # издержки

if proceeds > spending:
    print("Profit")
    profit_margin = (proceeds - spending) / proceeds  # рентабельность
    print(f"Profit margin is {round(profit_margin, 2)}")
    number_of_staff = int(input("Enter Number of Staff: "))  # количество сотрудников
    profit_for_one_worker = (proceeds - spending) / number_of_staff
    print(f"Profit for one worker {round(profit_for_one_worker, 2)}")   # прибыль на одного сотрудника
elif proceeds < spending:
    print("Losses")
else:
    print("Zero balance")
