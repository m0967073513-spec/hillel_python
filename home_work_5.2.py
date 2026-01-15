
# ДЗ 5.2. Модифікувати калькулятор

while True:
    x = float(input("Введіть перше число: "))
    y = float(input("Введіть друге число: "))
    operator = input("Введіть дію (+, -, *, /): ")

    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "*":
        print(x * y)
    elif operator == "/":
        if y != 0:
            print(x / y)
        else:
            print("Ділення на нуль неможливе")
    else:
        print("Невідома операція")

    choice = input("Бажаєте продовжити? (yes / y — так, no — ні): ").lower()
    if choice not in ("yes", "y"):
        print("Роботу калькулятора завершено")
        break
