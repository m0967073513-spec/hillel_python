
# ДЗ 7.4. Пошук спільних елементів

def common_elements():
    s1 = {x for x in range(100) if x % 3 == 0}
    s2 = {x for x in range(100) if x % 5 == 0}
    return s1 & s2

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
