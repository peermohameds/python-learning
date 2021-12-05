"""
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
"""
# wikimass solution. i was blank
for i in range(1, 6):
    print(i, end=" ")
    m = 4
    k = m + i
    for j in range(1, i ):
        print(k, end=" ")
        m -= 1
        k = m + k
    print()
