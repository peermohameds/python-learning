class Car:
    def __init__(self, make, model, year, sku):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__sku = sku

    # definition of getter

    def get_make(self):
        return self.__make

    # definition of setter

    def set_make(self, value):
        self.__make = value

    make = property(get_make, set_make)  # created property make


swift = Car('Maruti', 'Swift', '2013', '12344234')
swift.make = 'Maruti Suzuki'
print(swift.make)