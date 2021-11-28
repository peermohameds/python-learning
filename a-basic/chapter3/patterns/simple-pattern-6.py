'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
rows = int(input('Enter number : '))
print("using for loop")
print("*" * 30)

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(i, end=" ")
    print()

print("using while loop")
print("*" * 30)
i = rows
while i > 0:
    j = i
    while j > 0:
        print(i, end=" ")
        j -= 1
    i -= 1
    print()
