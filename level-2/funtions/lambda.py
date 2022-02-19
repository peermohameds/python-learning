from functools import  reduce

double_num = lambda n: n*2
print(double_num(2))

is_even = lambda n: n % 2 == 0
print(is_even(5))

_list = [2, 4, 5, 0, 72, 11, 31, 223]
# filter
even_list = filter(is_even, _list)
print(list(even_list))
print(list(filter(lambda n: n % 2 == 1, _list)))

# map
print(list(map(lambda n: n * 2, _list)))

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 8)))
print(result)

# reduce
print(reduce(lambda x, y: x+y, _list))

_names = ['peer', 'syed']
print(list(map(str.capitalize, _names)))
