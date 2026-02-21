
# HW 12.2. Корзина для покупок


class Item:
    def __init__(self, name, price, description="", dimensions=""):
        self.name = name
        self.price = float(price)
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price:g}"

    def __hash__(self):
        return hash(self.name.lower())

    def __eq__(self, other):
        return isinstance(other, Item) and self.name.lower() == other.name.lower()


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item(self, item, cnt=1):
        if cnt <= 0:
            raise ValueError("cnt must be > 0")

        self.products[item] = cnt

    def set_item(self, item, cnt):
        """(0 = удалить)"""
        if cnt < 0:
            raise ValueError("cnt must be >= 0")

        if cnt == 0:
            self.products.pop(item, None)
        else:
            self.products[item] = cnt

    def remove_item(self, item, cnt=1):
        if cnt <= 0:
            raise ValueError("cnt must be > 0")

        if item not in self.products:
            return

        new_cnt = self.products[item] - cnt
        if new_cnt <= 0:
            del self.products[item]
        else:
            self.products[item] = new_cnt

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        lines = [f"User: {self.user}", "Items:"]
        for item, cnt in self.products.items():
            lines.append(f"{item.name}: {cnt} pcs.")
        return "\n".join(lines)


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon) 

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
print(cart)

cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
print(f"Total: {cart.get_total()}")
assert cart.get_total() == 60, 'Повинно залишатися 60!'
print(cart.get_total())

cart.add_item(apple, 10)
print(cart)

assert cart.get_total() == 40

print("OK")