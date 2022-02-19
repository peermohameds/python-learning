def func(*param):
    return sum(param)


def person(**param):
    for key, value in param.items():
        print(f"{key}: ", value)


print("Three arguments", func(2, 3, 4))
print("5 arguments", func(2, 3, 4, 8, 9))
person(name="peer", age=42)

