"""
1 1 1 1 1
2 2 2 2
3 3 3
2 2
1
"""
for i in range(1, 6):
    for j in range(5, i-1, -1):
        if i < 4:
            print(i, end=" ")
        else:
            print(6-i, end=" ")
    print()
