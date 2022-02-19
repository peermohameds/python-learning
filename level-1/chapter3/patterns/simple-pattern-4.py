'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''

rows = int(input('Enter no of rows: '))
print("using for loop")
print("*" * 30)
for i in range(rows, 0, -1):
    for j in range(0, i+1):
        print(j, end=" ")
    print()

# same program using while
print()
print("using while loop")
print("*" * 30)
i = rows
while i >= 1:
    j = 0
    while j <= i:
        print(j, end=" ")
        j += 1
    i -= 1
    print()