class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__pushcount = 0
        self.__popcount = 0

    def get_counter(self):
        #
        # Present the counter's current value to the world.
        #
        # print("Push Count:", self.__pushcount)
        # print("Pop Count:", self.__popcount)
        return self.__pushcount, self.__popcount

    def pop(self):
        #
        # Do pop and update the counter.
        #
        Stack.pop(self)
        self.__popcount += 1

    def push(self, value):
        Stack.push(self, value)
        self.__pushcount += 1


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())