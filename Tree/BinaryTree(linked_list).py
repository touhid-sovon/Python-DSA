# Binary tree using Linked List

import Queue.Queue_Linked_list as queue


class TreeNode:
    def __init__(self,data = None):
        self.data = data
        self.right = None
        self.left = None

drinks = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
coke = TreeNode("Coke")
pepsi = TreeNode("Pepsi")

drinks.left = hot
drinks.right = cold
hot.left = tea
hot.right = coffee
cold.left = coke
cold.right = pepsi



def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


#preOrderTraversal(drinks)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)

#inOrderTraversal(drinks)

def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)


#postOrderTraversal(drinks)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return

    customQ = queue.QueueLinkedList()
    customQ.enqueue(rootNode)

    while not (customQ.isEmpty()):
        root = customQ.dequeue()
        print(root.data)
        if (root.left is not None):
            customQ.enqueue(root.left)
        if (root.right is not None):
            customQ.enqueue(root.right)

#levelOrderTraversal(drinks)

def search(rootNode,value):
    if not rootNode:
        return "The Tree is Empty"

    customQ = queue.QueueLinkedList()
    customQ.enqueue(rootNode)

    while not (customQ.isEmpty()):
        root = customQ.dequeue()

        if root.data == value:
            return "Found"
        if root.left:
            customQ.enqueue(root.left)
        if root.right :
            customQ.enqueue(root.right)


    return "Not Found"


# print(search(drinks,"Pepsi"))

def insert(rootNode,value):
    if not rootNode:
        return "The Tree is empty"

    newNode = TreeNode(value)
    customQ = queue.QueueLinkedList()
    customQ.enqueue(rootNode)

    while not (customQ.isEmpty()):
        root = customQ.dequeue()

        if root.left:
            customQ.enqueue(root.left)
        else:
            root.left = newNode
            return

        if root.right:
            customQ.enqueue(root.right)
        else:
            root.right = newNode
            return



#levelOrderTraversal(drinks)

def deepestNode(rootNode):
    if not rootNode:
        return

    customQ = queue.QueueLinkedList()
    customQ.enqueue(rootNode)
    lastNode = None
    while not (customQ.isEmpty()):
        lastNode = customQ.dequeue()
        if lastNode.left:
            customQ.enqueue(lastNode.left)
        if lastNode.right:
            customQ.enqueue(lastNode.right)

    return lastNode.data

def deleteDeepestNode(rootNode):
    if not rootNode:
        return

    customQ = queue.QueueLinkedList()
    customQ.enqueue(rootNode)
    targetNode = deepestNode(rootNode)
    print("Target Node",targetNode)

    while not (customQ.isEmpty()):
        lastNode = customQ.dequeue()

        if lastNode.left:
            if lastNode.left == targetNode:
                print("yes")

            else:
                customQ.enqueue(lastNode.left)
        if lastNode.right:
            if lastNode.right == targetNode:
                print("Yes")
                lastNode.data.right = None
            else:
                customQ.enqueue(lastNode.right)


print("The deepest Node:-- ",deepestNode(drinks))

deleteDeepestNode(drinks)

levelOrderTraversal(drinks)












