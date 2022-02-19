def get_number():
    try:
        return 1 / int(input('Enter Whole No: '))
    except ValueError:
        print('Given was not an integer')
    except ZeroDivisionError:
        print('Zero is not a valid integer')
    except:
        print('Too Bad')


print(get_number())
