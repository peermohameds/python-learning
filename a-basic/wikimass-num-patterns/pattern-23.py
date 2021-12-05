"""
1 2 3 4 5 5 4 3 2 1
1 2 3 4 * * 4 3 2 1
1 2 3 * * * * 3 2 1
1 2 * * * * * * 2 1
1 * * * * * * * * 1
"""
# my solution
for i in range(1, 6):
    for j in range(1, 7 - i):
        print(j, end=" ")
    for k in range(i, 1, -1):
        print("*", end=" ")
    for l in range(1, i):
        print("*", end=" ")
    for m in range(6-i, 0, -1):
        print(m, end=" ")
    print()
# wikimass solution
for i in range(6, 1, -1):
    for j in range(1, i):
        print(j, end=" ")
    for k in range(i, 6):
        print("**", end=" ")
    for m in range(i-1, 0, -1):
        print(m, end="")
    print()


