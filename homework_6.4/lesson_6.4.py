# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
digits_list = [1,5,12,45,3,78]
even_numbers = []

for num in digits_list:
    if num % 2 == 0:
        even_numbers.append(num)
total = sum(even_numbers)
print(total)


