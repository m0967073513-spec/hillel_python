
# ДЗ 6.1. Діапазон букв

import string

leters = string.ascii_letters

a,b = input("Введіть коректне імя: ").split("-")

print(leters[leters.index(a):leters.index(b)+1])



