'''
Multi line comment 
to enter who wrote the script
'''
i = 1
skip_num = int(input("Enter number between 1..10 to hop the loop"))
while i <= 10:
    if i == skip_num :
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("Exited Loop")