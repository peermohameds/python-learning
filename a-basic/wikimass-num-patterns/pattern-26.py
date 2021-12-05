"""
5 4 3 2 *
5 4 3 * 1
5 4 * 2 1
5 * 3 2 1
* 4 3 2 1
"""
for i in range(1, 6):
    for j in range(5, 0, -1):
        if i == j:
            print("*", end=" ")
        else:
            print(j, end=" ")
    print()
