"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
# my logic. Bit big
for i in range(1, 6):
    for j in range(1, i + 1):
        if i % 2 == 0:
            if j % 2 == 0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        else:
            if j % 2 == 1:
                print(1, end=" ")
            else:
                print(0, end=" ")
    print()

# wikimass login. Simple
for i in range(1, 6):
    for j in range(i, i + i):
        print(j % 2, end=" ")
    print()