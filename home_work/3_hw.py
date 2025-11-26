def find_max_number(a, b):

    """Функция принимает два числа и выводит наибольшее из них"""

    if a > b:
        print(f"Наибольшее число: {a}")
    else:
        print(f"Наибольшее число: {b}")


find_max_number(17, 9)
find_max_number(4, 11)


def check_difference(a, b):

    """Функция проверяет, отличаются ли числа на 135"""

    if abs(a - b) == 135:
        print("yes")
    else:
        print("No")


check_difference(100, 235)
check_difference(100, 240)


def get_season(month):

    """ Функция определяет сезон года по номеру месяца"""
    if month == 12 or month == 1 or month == 2:
        print("зима")
    elif month == 3 or month == 4 or month == 5:
        print("весна")
    elif month == 6 or month == 7 or month == 8:
        print("лето")
    elif month == 9 or month == 10 or month == 11:
        print("осень")
    else:
        print("Неверный номер месяца")

get_season(1)
get_season(3)


def check_numbers(a, b, c):

    """Функция проверяет, все ли числа больше 10"""

    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")


check_numbers(15, 20, 25)
check_numbers(11, 12, 13)

