"""
1 2 3 4 5 6 7
1 2 3 4 5
1 2 3
1
"""

for i in range(7, 0, -2):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
