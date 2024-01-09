class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def  __len__(self):
        node = self.head
        len = 0
        while node:
            node = node.next
            len += 1
        return len

    def __str__(self):
        if self.head is None:
            return "[]"
        else:
            values = [str(x) for x in (self)]
            return '\n'.join(values)

    def push(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            newNode.next = None
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            return "The Stack Is Empty"
        else:
            popNode = self.head.value
            self.head = self.head.next
            return popNode

    def peek(self):
        if self.head is None:
            return "The Stack Is Empty"
        else:
            return self.head.value

    def isEmpty(self):
        if self.head is None:
            return "The Stack is empty"
        else:
            return "The Stack is not empty"


    def delete(self):
        self.head = None

stackLinkedList = StackLinkedList()

stackLinkedList.push(1)
stackLinkedList.push(2)
stackLinkedList.push(3)
stackLinkedList.push(4)

print(len(stackLinkedList))

print("The pop value",stackLinkedList.pop())


print("The length :",len(stackLinkedList))

print(stackLinkedList)

print("The peek Value",stackLinkedList.peek())

stackLinkedList.delete()

print(stackLinkedList)
