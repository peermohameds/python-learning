def raise_error(num):
    try:
        a = 1/num
    except ZeroDivisionError:
        print('Zero')
    except:
        print('Summa')
    else:
        print('Success')
    finally:
        print('Completed')


#raise_error(0)

class Ex(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.args =(args, )
