# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

my_input = input('Please enter words: "Happy hamster": ')

found = False
for i in my_input:
    if i == "h" or i == "H":
        found = True
        break
if found:
    print("You are right")
else:
    print("You are wrong")

