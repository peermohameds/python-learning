'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
rows = int(input('Enter number : '))
print("using for loop")
print("*" * 30)
for i in range(1, rows+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# same using while loop
print("using for loop")
print("*" * 30)
i = 1
while i <= rows:
    j = i
    while j >= 1:
        print(j, end=" ")
        j -= 1
    i += 1
    print()

