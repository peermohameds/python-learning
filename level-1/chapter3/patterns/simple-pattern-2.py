'''
Print pattern as below
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''

rows = int(input('Enter a number: '))
print("using for loop")
print("*" * 30)
b = 0
# for loop to print rows descending order
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i+1):
        print(b, end=" ")
    print()

# same program using while
print()
print("using while loop")
print("*" * 30)
i = rows
b = 1
while i >= 1:
    j = i
    while j >= 1:
        print(b, end=" ")
        j -= 1
    i -= 1
    b += 1
    print()
