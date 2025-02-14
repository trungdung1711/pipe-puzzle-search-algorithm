class Stack:
    def __init__(self):
        self.__items = []


    def push(self, item):
        self.__items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        else:
            raise IndexError('Pop from empty stack')
        

    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        else:
            raise IndexError('Peek from empty stack')


    def is_empty(self):
        return len(self.__items) == 0
    

    def size(self):
        return len(self.__items)