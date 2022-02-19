import json


class Super:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return "I am {}".format(self.name)


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub('Peer')
print(obj)

print(json.dumps(dir(obj), indent=4))
