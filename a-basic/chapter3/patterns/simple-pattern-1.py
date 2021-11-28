'''
print patter like below.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
number = int(input('Enter a Number: '))

# Loop to print rows
for i in range(1, number+1):
    # Loop to print columns
    for j in range(i):
        print(j+1, end=" ")
    print()
