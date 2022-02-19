class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        temp = self.__queue[0]
        del self.__queue[0]
        return temp

    def isempty(self):
        return len(self.__queue) == 0


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")