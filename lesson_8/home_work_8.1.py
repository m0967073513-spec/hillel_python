
# ДЗ 8.1. Додати 1 до числа

def add_one(some_list):
    if some_list == []:
        return [1, 0]


    res = some_list[:]
    carry = 1

    for i in range(len(res) - 1, -1, -1):
        s = res[i] + carry
        res[i] = s % 10
        carry = s // 10
        if carry == 0:
            break

    if carry:
        res = [carry] + res

    return res

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([]) == [1, 0], "Test4"
print("OK")
