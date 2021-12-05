"""
5 5 5 5 5
4 5 5 5 5
3 4 5 5 5
2 3 4 5 5
1 2 3 4 5
"""
for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end=" ")
    for k in range(1, i):
        print(5, end=" ")
    print()
