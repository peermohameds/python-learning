"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
m = 0
for i in range(5, 0, -1):
    for j in range(i + m, m, -1):
        print(j, end=" ")
    m += 1
    print()