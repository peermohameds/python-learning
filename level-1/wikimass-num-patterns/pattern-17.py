"""
1 3 5 7 9
3 5 7 9
5 7 9
7 9
9
"""
for i in range(1, 10, 2):
    for j in range(i, 10, 2):
        print(j, end=" ")
    print()
