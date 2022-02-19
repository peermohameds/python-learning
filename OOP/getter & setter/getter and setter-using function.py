class Item:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    price = property(get_price, set_price)


item1 = Item("Dell", 799.99)
print(item1.price)
item1.price=899.99
print(item1.price)
