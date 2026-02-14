
# 11.1. Генератор простих чисел

from inspect import isgenerator

def prime_generator(end):
    for n in range(2, end + 1):
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
print(list(prime_generator(10)))
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
print(list(prime_generator(15)))
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print(list(prime_generator(29)))
print('Ok')

# другий варіант з використанням решета Ератосфена

def prime_generator(end):
    if end < 2:
        return 

    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, end + 1):
        if sieve[num]:
            yield num
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
print(list(prime_generator(10)))
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
print(list(prime_generator(15)))
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print(list(prime_generator(29)))
print('Ok')


