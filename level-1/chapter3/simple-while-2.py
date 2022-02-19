# get number input until -1 is entered
# check the largest value entered

largest_number = -9999999999999

number = int(input("Enter number or -1 to exit"))

while number != -1:
    if number > largest_number:
        largest_number = number

    number = int(input("Enter number or -1 to exit"))

print("largest number is",largest_number)
