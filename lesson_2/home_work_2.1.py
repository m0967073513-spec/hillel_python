

import math

# 1. Квадрат числа
user_input = input("введіть число для возведения в квадрат: ")
a=int(user_input)
print(a*a)

    
# 2. Середнє трьох чисел
user_input1 = input("введіть перше число: ")
user_input2 = input("введіть друге число: ")
user_input3 = input("введіть третє число, для виводу їх середнього арифметичного: ")
a=int(user_input1)
b=int(user_input2)
c=int(user_input3)
print((b+a+c)/3)


# 3. Перетворення хвилин у години
user_input4 = input("введіть кількість хвилин: ")
a=int(user_input4)
b= 60
print(a//b, "год", a % b, "хв")


# 4. Розрахунок знижки 
user_input5 = input("введіть ціну товару: ")
user_input6 = input("введіть розмір знижки у відсотках: ")
a=int(user_input5)
b=int(user_input6)
print(a - (a * b / 100))


# 5. Остання цифра числа (При тестуванні зявилася проблема с отрецательним числом, знайшов рішення функція abs() та використав)
user_input7 = input("введіть ціле число: ")
a=int(user_input7)
a=abs(a)
print(a % 10) 


# 6. Периметр прямокутника 
user_input8 = input("введіть довжину прямокутника: ")
user_input9 = input("введіть ширину прямокутника: ")
a=int(user_input8)
b=int(user_input9)
print(2*(a+b))


# 7. Виведення числа в стовпчик
user_input10 = input("введіть чотирьохзначне число: ")
a=int(user_input10)
print(a // 1000)
print((a // 100) % 10)
print((a // 10) % 10)
print(a % 10)

print("The_end")
