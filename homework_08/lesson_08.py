# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток
# і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

def sum_of_digits(*args):
    for item in args:
        try:
            numbers = []
            parts = item.split(',')
            for x in parts:
                numbers.append(int(x))
            print(sum(numbers))
        except ValueError:
                print("I can't do it")
sum_of_digits("1,2,3,4", "1,2,3,4,50", "qwerty1,2,3")

