i = 1
breaker = int(input("Enter breaking point between 1..10: "))
while i <= 10:
    print("Loop ", i)
    if i == breaker:
        break
    i+=1
print("Exited Loop")