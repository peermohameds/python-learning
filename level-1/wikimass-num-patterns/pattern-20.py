"""
1
2 3
4 5 6
7 8 9 10
"""
m = 1
for i in range(1, 5):
    for j in range(1, i + 1):
        print(m, end=" ")
        m += 1
    print()
