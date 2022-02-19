'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
rows = int(input('Enter number : '))
print("using for loop")
print("*" * 30)
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# same using while loop
print()
print("using for loop")
print("*" * 30)
i = rows
while i > 0:
    j = i
    while j > 0:
        print(j, end=" ")
        j -= 1
    i -= 1
    print()