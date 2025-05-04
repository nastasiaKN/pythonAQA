# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from operator import index


def multiplication_table(number):
    multiplier = 1

    while number * multiplier <= 25:
        result = number * multiplier
        print(f"{number}x{multiplier}={result}")
        multiplier += 1
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def count_function(number1, number2):
    print(number1 + number2)
count_function(5, 89)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def my_arithmerics(*numbers):
    print(sum(numbers) / len(numbers))
my_arithmerics(3,5,68,9.7)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def my_function1(reverse_string: str):
    return(reverse_string[::-1])
print(my_function1("hello"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def my_function2(words: list[str]):
    print(len(words))
    return max(words, key=len)
my_function2(["Hello", "how", "are", "you", "doing","I", "am", "overhelelmed"])

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
def define_unique_symbols():
    entered_words = input("input you phrase: ")
    unique_symbols = set(entered_words)
    if len(unique_symbols) > 10:
        print(True)
    else:
        print(False)
define_unique_symbols()

# task 8
def sort_by_even_numbers(*digits_list):
    even_numbers = []
    for num in digits_list:
        if num % 2 == 0:
            even_numbers.append(num)
    total = sum(even_numbers)
    return total
result = sort_by_even_numbers(1, 5, 12, 45, 3, 78)
print(result)

# task 9

def salary_calculation(monthly_payment: int):
    total_sum = monthly_payment * 18
    return total_sum
result = salary_calculation(1200)
print(f"{result}")

# task 10

def students_presence(boys_total: int, boys_absent: int, girls_absent: int):
    girls_total = boys_total // 2
    today_present = (boys_total - boys_absent) + (girls_total - girls_absent)
    return today_present
total_present = students_presence(24,2,2)
print(total_present)
