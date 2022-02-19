"""
    1
  2 3 4
5 6 7 8 9
"""
k = 0
for i in range(1, 6, 2):
    for j in range(5, 0, -1):
        if j > i:
            print(" ", end="")
        else:
            k += 1
            print(k, end=" ")
    print()
