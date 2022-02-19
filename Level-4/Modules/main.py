from sys import path
import tally
path.append("../custom")
from custmodule import suml, prodl

print('Running', __name__)
zeros = [i for i in range(1, 6)]
ones = [i for i in range(1, 10)]
print(suml(zeros))
print(prodl(ones))

for p in path:
    print(p)



