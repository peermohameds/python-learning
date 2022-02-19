class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val
        self.__first = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

# class does not have __first, whereas object does not have varia
print(ExampleClass.__dict__)
print(example_object.__dict__)

# creating another instance will overwrite class class variable 'varia'
example_object_1 = ExampleClass(4)
print(ExampleClass.__dict__)
print(example_object_1.__dict__)

example_object_1._ExampleClass__first = 10
print(example_object_1.__dict__)

# Does example_object_1 have property alpha?
print(hasattr(example_object_1, 'alpha'))
