# ДЗ 5.1. Ім'я змінної

import string
import keyword

while True:
    name = input("Введіть коректне ім'я змінної: ")
    bad_punct = string.punctuation.replace("_", "")
    is_valid = True

    if name == "":
        is_valid = False

    elif name in keyword.kwlist:
        is_valid = False

    elif name[0].isdigit():
        is_valid = False

    elif any(ch.isupper() for ch in name):
        is_valid = False

    elif any(ch.isspace() or ch in bad_punct for ch in name):
        is_valid = False

    elif set(name) == {"_"} and len(name) > 1:
        is_valid = False

    print(is_valid)

    choice = input("Бажаєте продовжити? (yes / y — так, no — ні): ").lower()
    if choice not in ("yes", "y"):
        print("Роботу завершено")
        break

# Обгорнув у цикл while для зручності тестування
    
