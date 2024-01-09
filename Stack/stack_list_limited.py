class StackLimited:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    # is empty
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    # is full
    def isFull(self):
        if len(self.list) == self.maxSize:
            return "The Stack is full"
        else:
            return False

    # display
    def __str__(self):
        if self.isEmpty():
            return "[]"
        else:
            values = [str(x) for x in reversed(self.list)]
            return '\n'.join(values)

    # push
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The value is inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]

    # delete
    def delete(self):
        self.list = []

stacktLimit = StackLimited(5)
stacktLimit.push(1)
stacktLimit.push(2)
stacktLimit.push(3)
stacktLimit.push(4)
stacktLimit.push(5)
print(stacktLimit.isFull())
print(stacktLimit.push(6))

print("The pop value:",stacktLimit.pop())

print(stacktLimit)


print("The pop value:",stacktLimit.pop())

print(stacktLimit)

print("The Peek value",stacktLimit.peek())

stacktLimit.delete()

print(stacktLimit)