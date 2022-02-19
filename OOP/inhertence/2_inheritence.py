class Item:
    children = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        assert quantity >= 0, f"Quantity cannot be a negative number"
        assert price > 0, f"Price cannot be a 0 or negative number"

        self.name = name
        self.price = price
        self.quantity = quantity
        Item.children.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, damaged_count=0) -> None:
        super().__init__(name, price, quantity)
        # assert quantity >= 0, f"Quantity cannot be a negative number"
        # assert price > 0, f"Price cannot be a 0 or negative number"
        assert damaged_count >= 0, f"Price cannot be a 0 or negative number"

        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.damaged_count = damaged_count

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity}, {self.damaged_count})"

class Laptop(Item):
    def __init__(self, name: str, price: float, quantity=0, damaged_count=0, has_numpad=False):
        super().__init__(name, price, quantity)
        assert damaged_count >= 0, f"Price cannot be a 0 or negative number"

        self.damaged_count = damaged_count
        self.has_numpad = has_numpad

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity}, {self.damaged_count}, {self.has_numpad})"


phone1 = Phone("Samsung S10", 599, 12, 1)
laptop1 = Laptop('Dell', 799, 12, 0, True)
print(phone1)
print(Item.children)