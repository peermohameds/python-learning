"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""
m = 1
for i in range(5, 0, -1):
    for j in range(m, i + m):
        print(j, end=" ")
    m += 1
    print()
