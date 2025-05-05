# homework_3

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
def total_sea_area(black_sea_km2, azov_sea_km2):
    return black_sea_km2 + azov_sea_km2
print(total_sea_area(436402, 37800))

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
def calculate_items_per_warehouse(total_items, total_s1_s2, total_s2_s3):
    s1 = total_items - total_s2_s3
    s2 = total_s1_s2 - s1
    s3 = total_s2_s3 - s2
    return s1, s2, s3

s1, s2, s3 = calculate_items_per_warehouse(375291, 250449, 222950)
print(f"{s1},{s2},{s3}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def calculate_total_price(monthly_payment, months):
    return monthly_payment * months

total_sum = calculate_total_price(1179, 18)
print(total_sum)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

def remain_from_num_devision(remaining):
    return remaining
a = 8019
b = 9907
c = 2789
d = 7248
e = 7128
f = 19224
remaining = remain_from_num_devision([a % 8,b % 9,c % 5,d % 6,e % 5,f % 9])
print(remaining)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
def count_total_order_price(prices, counts):
    total = 0
    for item in prices:
        total += prices[item] * counts[item]
    return total

order_and_price = {
    "pizza_L": 274,
    "pizza_M": 218,
    "juice": 35,
    "cake": 350,
    "water": 21
}

item_count = {
    "pizza_L": 4,
    "pizza_M": 2,
    "juice": 4,
    "cake": 1,
    "water": 3
}

total_order = count_total_order_price(order_and_price, item_count)
print(total_order)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

all_photos = 232
photos_per_page = 8
total_pages = all_photos // photos_per_page
print(f"{total_pages}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
def road_trip_stats(distance, liters_per_100km, fuel_tank_liters):
    return (distance / 100) * liters_per_100km, int(((distance / 100) * liters_per_100km + fuel_tank_liters - 1) // fuel_tank_liters)

fuel, refuels = road_trip_stats(1600, 9, 48)
print(round(fuel, 2))
print(refuels)

# homework_6.2
# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

def has_h(word):
    return 'h' in word.lower()


# homework_6.3
# Є list з даними lst1 =
# ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

def add_string_items_to_the_list(lst_str):
    return [item for item in lst_str if isinstance(item, str)]

lst_str = add_string_items_to_the_list(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
print(lst_str)


# homework_6.4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

def even_numbers_from_list(numbers):
    return [num for num in numbers if num % 2 == 0]

total = even_numbers_from_list([1, 5, 12, 45, 3, 78])
print(total)


