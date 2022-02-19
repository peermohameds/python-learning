class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.__price = price
        self.quantity = quantity

    # readonly attribute use of @property decorator
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 15:
            raise Exception('Name is too long')
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def increase_price(self, increment_value):
        self.__price = self.__price  + self.__price * increment_value


item1 = Item('Samsung S10', 100, 12)
print(item1.name)
item1.increase_price(0.2)
print(item1.price)