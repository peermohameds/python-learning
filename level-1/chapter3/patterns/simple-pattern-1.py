'''
print patter like below.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
number = int(input('Enter a Number: '))
print("using for loop")
print("*" * 30)
# Loop to print rows
for i in range(1, number+1):
    # Loop to print columns
    for j in range(i):
        print(j+1, end=" ")
    print()

# same program using loop
i = 1

# same program using while
print()
print("using while loop")
print("*" * 30)
while i <= number:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    i += 1
    print()