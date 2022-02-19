"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""
m = 1
for i in range(5, 0, -1):
    for j in range(i, i + m):
        print(j, end=" ")
    m += 1
    print()

"""
Website Answer:
for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end="")
    print()
"""
