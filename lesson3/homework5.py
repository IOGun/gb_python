# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.

def special_symbol(input_string):
    """
    Return True if special symbol in input_string and False if it isn't
    :param input_string: str
    :return: bool
    """
    result = False
    for ch in ["!", "@", "#", "$", "%", "^", "&", "*"]:
        # print(f"{ch}  {input_string}")
        if ch in input_string:
            result = True
            break
    return result

def my_func(input_string):
    """
    Return sum of numbers in input_string
    :param input_string: str
    :return: int
    """
    my_list = input_string.split(' ')
    result = 0
    for num in my_list:
        if special_symbol(num):
            break
        result += int(num)
    return result

result = 0

while True:
    input_str = input("""Special symbols: "!", "@", "#", "$", "%", "^", "&", "*"
Enter your string (for exit enter special symbol): """)
    result += my_func(input_str)
    if special_symbol(input_str):
        break
    print(result)

print(result)