def print_name(firstname="peer", lastname="syed"):
    print("Hello", lastname, ",", firstname)

# positional arguments
print_name("John", "Doe")
# keyword arguments
print_name(firstname="John", lastname="Doe")

# positional + keyword arguments
# a positional argument cannot be passed after using keywork argument
# that will throw syntax error
print_name("John", lastname="Doe")