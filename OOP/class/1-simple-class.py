class HelloWorld:
    def __init__(self):    # constructor
        # print("Hello World")
        self.stack_list = []
        self.__hidden_prop = 'Hello'

    def get_hidden(self):  # sample method
        print(self.__hidden_prop)


my_class = HelloWorld()
my_class.get_hidden()