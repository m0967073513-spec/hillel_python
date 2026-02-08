
# ДЗ 10.3. Перевірити чи є парним чи ні

def is_even(digit):
    """Перевірка чи є парним число"""
    return (digit & 1) == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

# Побітове порівняння яке ми розбирали на прошлому уроці. Якщо останній біт числа 0, то число парне, якщо 1 - непарне.
