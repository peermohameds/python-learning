class ShopItem:
    discount_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        # assert values
        assert price >= 0, f"price {price} is less than 0"
        assert quantity >= 0, f"quantity {quantity} is less than 0"

        # initialize values
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount_rate


object1 = ShopItem('Pen', 11.0, 57)
object1.discount_rate = 0.5
object1.apply_discount()
print(f"Rs. {object1.calculate_total()}")

object2 = ShopItem('Pen Stand', 113.0, 6)
print(f"Rs. {object2.calculate_total()}")
object2.apply_discount()
print(f"Rs. {object2.calculate_total()}")

