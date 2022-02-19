'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
'''

rows = int(input('Enter number : '))
print("using for loop")
print("*" * 30)
b = 1
for i in range(1, rows + 1):
    for j in range(1, i+1 ):
        print(b, end=" ")
    b += 2
    print()

# same using while
print("using for loop")
print("*" * 30)
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(i * 2 - 1, end=" ")
        j += 1
    i += 1
    print()
