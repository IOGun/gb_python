# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_func(name, surname, year, city, mail, phone):
    """
    Format users information
    :param name: str
    :param surname: str
    :param year: str
    :param city: str
    :param mail: str
    :param phone: str
    :return: None
    """
    print(f"{surname} {name} born in {year}. Contact phone number is {phone}, Email is {mail}")

user_dict = {"name":"Ivan",
             "surname":"Ivanov",
             "year":"2021",
             "city":"New York",
             "mail":"Ivanov@mail.net",
             "phone":"8(888)888-88-88"
             }

for key in user_dict:
    user_dict[key] = input(f"Enter your {key} (Example: {user_dict[key]}): ")

user_func(
    name=user_dict["name"],
    surname=user_dict["surname"],
    year=user_dict["year"],
    city=user_dict["city"],
    mail=user_dict["mail"],
    phone=user_dict["phone"]
)
