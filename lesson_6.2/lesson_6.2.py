# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

my_input_char = input('Please enter words with h/H: ')
while 'h' not in my_input_char.lower():
    my_input_char = input('Please enter words with h/H: ')

print(my_input_char)
print("You are right")











