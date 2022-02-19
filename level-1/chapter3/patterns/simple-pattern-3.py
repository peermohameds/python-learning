'''
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
'''
rows = int(input('Enter no of rows: '))
print("using for loop")
print("*" * 30)
# loop for rows in rev order
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(rows, end=" ")
    print()

# same program using while
print()
print("using while loop")
print("*" * 30)
i = rows

while i >= 1:
    j = i
    while j >= 1:
        print(rows, end=" ")
        j -= 1
    i -= 1
    print()

