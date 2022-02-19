class Item:
    discount_rate = 0
    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        return self.price - self.price * self.discount_rate


class Phone(Item):
    discount_rate = 0.2

    def __init__(self, name: str, price: float, quantity=0):
        super(Phone, self).__init__(name, price, quantity)


class Laptop(Item):
    discount_rate = 0.1

    def __init__(self, name: str, price: float, quantity=0):
        super(Laptop, self).__init__(name, price, quantity)

    def apply_discount(self):
        return super(Laptop, self).apply_discount() + 40


phone1 = Phone(name='Samsung S10', price=600, quantity=12)
print(phone1.apply_discount())
laptop1 = Laptop('Dell', 800, 10)
print(laptop1.apply_discount())