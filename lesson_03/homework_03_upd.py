#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = "\"Would you tell me, please, which way I ought to go from here?\"\n" \
                      "\"That depends a good deal on where you want to get to,\" said the Cat.\n" \
                      "\"I don\'t much care where ——\" said Alice.\n" \
                      "\"Then it doesn\'t matter which way you go,\" said the Cat.\n" \
                      "\"—— so long as I get somewhere,\" Alice added as an explanation.\n" \
                      "\"Oh, you\'re sure to do that,\" said the Cat, \"if you only walk long enough.\""

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for char in alice_in_wonderland:
    if char == "'":
        print(char) 

# task 03 == Виведіть змінну alice_in_wonderland на друк
print (f"{alice_in_wonderland}")

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total_sqr_km = black_sea + azov_sea
print(f"{total_sqr_km}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items = 375291
total_items_s1_and_s2 = 250449
total_items_s2_and_s3 = 222950

s1 = total_items - total_items_s2_and_s3  
s2 = total_items_s1_and_s2 - s1           
s3 = total_items_s2_and_s3 - s2       

print(f"{s1},{s2},{s3}")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
total_sum = monthly_payment * 18
print(f"{total_sum}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8 
b = 9907 % 9     
c = 2789 % 5     
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"{a},{b},{c},{d},{e},{f}")

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
pizza_size_L = 274
pizza_size_M = 218
juice = 35
cake = 350
water = 21

pizza_L_count = 4
pizza_M_count = 2
juice_count = 4
cake_count = 1
water_count = 3

total = (pizza_size_L * pizza_L_count) + (pizza_size_M * pizza_M_count) + (juice * juice_count) 
+ (cake * cake_count) + (water * water_count)
print(f"{total}")


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
distance = 1600 
liters_per_100km = 9 
fuel_tank_liters = 48 
total_fuel_needed = (distance / 100) * liters_per_100km
total_refuels = total_fuel_needed // fuel_tank_liters
print(f"{total_fuel_needed}, {total_refuels}")