# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

my_phrase = input("input you phrase: ")
unique_symbols = set(my_phrase)

if len(unique_symbols) > 10:
    print(True)
else:
    print(False)