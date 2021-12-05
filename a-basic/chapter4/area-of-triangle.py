def is_valid_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    if not is_valid_triangle(a, b, c):
        return None
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


print(heron(1., 1., 2. ** .5))
