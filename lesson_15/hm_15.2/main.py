
# ДЗ 15.2

from fraction import Fraction

def parse_fraction(text: str) -> Fraction:
    text = text.strip()
    if '/' not in text:
        raise ValueError("Введіть дріб в форматі a/b, наприклад 2/3")

    left, right = text.split('/', 1)

    a = int(left.strip())
    b = int(right.strip())

    if b == 0:
        raise ValueError("Знаменник не може бути 0")

    return Fraction(a, b)


def input_fraction(prompt: str) -> Fraction:
    while True:
        try:
            s = input(prompt)
            return parse_fraction(s)
        except ValueError as e:
            print(f"Помилка: {e}. Спробуй ще раз =)")


def main():
    print("Введіть дві дроби в форматі a/b (наприклад: 2/3)\n")

    f1 = input_fraction("Дробь 1: ")
    f2 = input_fraction("Дробь 2: ")

    print("\nРезультати:")
    print("f1 =", f1)
    print("f2 =", f2)

    print("\nОперації:")
    print("f1 + f2 =", f1 + f2)
    print("f1 - f2 =", f1 - f2)
    print("f1 * f2 =", f1 * f2)

    print("\nПорівняння:")
    print("f1 == f2:", f1 == f2)
    print("f1 <  f2:", f1 < f2)
    print("f1 >  f2:", f1 > f2)


if __name__ == "__main__":
    main()
