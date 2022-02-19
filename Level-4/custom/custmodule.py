"""
main module as sample
"""
__counter = 0


def suml(the_list):
    """
    Calculates sum of a list

    This function calculates sum of given numbers as list
    :param the_list: list of numbers
    :return: sum as integer
    """
    global __counter
    __counter += 1
    the_sum = 0
    for i in the_list:
        the_sum += i
    return  the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for i in the_list:
        prod *= i
    return prod


if __name__ == "__main__":
    print("I prefer to be a module.")
    my_list = [i + 1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

