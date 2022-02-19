from classymain import Classy, SuperOne, SuperTwo


class Sub(SuperOne, SuperTwo):
    pass


# use of __module__
print(Classy.__module__)
obj = Classy()
print(obj.__module__)

# use of __bases__
print(Sub.__bases__)

print(Classy.__bases__)


def cls_print(cls):
    print(cls.__name__, ":", end=" ")
    for n in cls.__bases__:
        print(n.__name__, end=" ")
    print()


cls_print(Sub)
cls_print(Classy)