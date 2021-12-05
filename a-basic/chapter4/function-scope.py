
x = 0
print(id(x), "=", x)


def fun():
    global x
    x = 1
    print('inside function:',x)
    print(id(x), "=", x)


fun()
print('outside: ', x)
print(id(x), "=", x)

x = 10
print('outside: ', x)
print(id(x), "=", x)
fun()
