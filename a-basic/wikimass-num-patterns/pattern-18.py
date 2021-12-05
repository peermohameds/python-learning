"""
1
2 4
1 3 5
2 4 6 8
1 3 5 7 9
"""
# my logic with if
for i in range(1, 6):
    if i % 2 == 1:
        for j in range(1, i * 2 + 1, 2):
            print(j, end =" ")
    else:
        for j in range(2, i * 2 + 1, 2):
            print(j, end =" ")
    print()

