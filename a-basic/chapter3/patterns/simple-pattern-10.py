"""
1
3 2
6 5 4
10 9 8 7
"""
m = 1
for i in range(1, 5):
    for j in range(1, i + 1):
        print(m, end=" ")
        m += 1
    print()
