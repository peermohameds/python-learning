"""
1 2 3 4 5
4 3 2 1
1 2 3
2 1
1
Note: watch out odd / even rows
"""

for i in range(5, 0, -1):
    if i % 2 == 1:
        for j in range(1, i + 1):
            print(j, end=" ")
    else:
        for j in range(i, 0, -1):
            print(j, end=" ")
    print()