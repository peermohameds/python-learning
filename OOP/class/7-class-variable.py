class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1

    def set_second(self, value):
        self.__second = value


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
example_object_3.set_second(10)
example_object_3.third = 12
# Three instances are created. Look at the counter value for all objects
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# 4th instance also created. Look at the counter value for all objects
example_object_4 = ExampleClass(4)
print('after 4th instance')
del example_object_3.third
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)