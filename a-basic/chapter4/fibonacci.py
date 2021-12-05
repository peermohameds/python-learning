def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    the_sum = 0
    n_min_one = n_min_two = 1
    for i in range(3, n+1):
        the_sum = n_min_one + n_min_two
        n_min_one, n_min_two = n_min_two, the_sum
    return the_sum


for i in range(1, 10):
    print(i, "->", fibonacci(i))

