# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of
# fruit possessed by John, Mary, and Adam respectively;
John = 10
Mary = 10
Adam = 10
# # having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
print(John,Mary,Adam,sep=",")
print("John =",John,"Mary =",Mary,"Adam =",Adam)
# now create a new variable named total_apples equal to addition of the three former variables.
total_apples = John + Mary + Adam
# print the value stored in total_apples to the console;
print("total_apples =",total_apples)
# experiment with your code: create new variables, assign different values to them, and perform various arithmetic
# operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line,
# e.g., "Total number of apples:" and total_apples
a = 3
b = 4
# Pythagorean theorem sqrt(a2 + b2)
c = ( a ** 2 + b ** 2 ) ** 0.5
print("pythogorean theorem c =",c,"(As this was exponentiated with 0.5 we got float in result)")

# a square + b square + 2ab
c = ( a * a ) + ( b * b ) + ( 2 * a * b )
print("a2 + b2 + 2ab =",c, "(as no float involed in calcualtion result is integer)")

# assign negative values and do the operations
a = -10
b = 4
c = a / b
print("a / b =", c)

a = 13
b = -4
c = a // b
print("a // b =", c)

a = 13
b = 4
c = a // b
print("a // b =", c)

# need your attention
a = 13
b = 4
c = a % b
print("a % b =", c)

# check the remainder value
a = -13
b = 4
c = a % b
print("a % b =", c)

# check the remainder value
a = 13
b = -4
c = a % b
print("a % b =", c)

# Lets see deep
n = -13
d = 4
q = n // d
r = n % d
print("-13 // 4 : q =", q, "r =",r) 
print("d * q + r = n : n = ", d * q + r )

n = 13
d = -4
q = n // d
r = n % d
print("13 // -4 : q =", q, "r =",r) 
print("d * q + r = n : n = ", d * q + r )


