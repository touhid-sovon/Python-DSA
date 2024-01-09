class Stack:
    def __init__(self):
        self.list = []

    # empty
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    # display
    def __str__(self):
        if self.isEmpty():
            return "[]"
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    # push
    def push(self, value):
        self.list.append(value)

    # pop
    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]

    # DELETE
    def delete(self):
        self.list = []

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)

print('Pop Value:', stack.pop())
print(stack)

print('Peek value:', stack.peek())

stack.delete()
print(stack)
