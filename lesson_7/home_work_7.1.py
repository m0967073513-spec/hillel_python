# ДЗ 7.1. Вітання

def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
print("OK")


if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(say_hi(name, age))

