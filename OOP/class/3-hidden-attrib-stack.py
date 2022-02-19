class StackClass:
    def __init__(self):
        self.__stack_list = []

    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        temp = self.__stack_list[-1]
        del self.__stack_list[-1]
        return temp

    def display(self):
        print(self.__stack_list)


class QueueClass:
    def __init__(self):
        self.__queue_list = []

    def push(self, value):
        self.__queue_list.append(value)

    def pop(self):
        temp = self.__queue_list[0]
        del self.__queue_list[0]
        return temp

    def display(self):
        print(self.__queue_list)


my_stack = StackClass()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.display()
my_temp = my_stack.pop()
print("Popped", my_temp)
my_stack.display()

my_queue = QueueClass()
my_queue.push(10)
my_queue.push(20)
my_queue.push(30)
my_queue.push(40)
my_queue.display()
my_temp = my_queue.pop()
print("Popped", my_temp)
my_queue.display()