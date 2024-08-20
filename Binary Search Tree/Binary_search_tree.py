""" Binary Search Tree"""

from Queue import Queue_Linked_list as queue

''' Creation '''

class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


'''insertion'''
def insert(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
        return "The Root value is added"
    elif nodeValue <= rootNode.data :
        if rootNode.left is None:
            rootNode.left = BST(nodeValue)
        else:
            insert(rootNode.left,nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = BST(nodeValue)
        else:
            insert(rootNode.right,nodeValue)

    return "Child Value is added"

''' Pre-Order Traversal '''

def preOrderTraverse(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraverse(rootNode.left)
    preOrderTraverse(rootNode.right)

''' Inorder Traversal '''
def inOrderTraverse(rootNode):
    if not rootNode:
        return
    inOrderTraverse(rootNode.left)
    print(rootNode.data)
    inOrderTraverse(rootNode.right)

'''Post Order Traversal '''
def postOrderTraverse(rootNode):
    if not rootNode:
        return
    postOrderTraverse(rootNode.left)
    postOrderTraverse(rootNode.right)
    print(rootNode.data)

'''Level Order Traversal'''
def levelOrderTraverse(rootNode):
    if not rootNode:
        return
    customQ = queue.QueueLinkedList()
    customQ.enqueue(rootNode)
    while not (customQ.isEmpty()):
        root = customQ.dequeue()
        print(root.data)
        if root.left:
            customQ.enqueue(root.left)
        if root.right:
            customQ.enqueue(root.right)

''' Search '''
def search(rootNode,value):
    if rootNode is None:
        return "Not Found"
    if rootNode.data == value:
        return "Found"
    elif value <= rootNode.data:
        return search(rootNode.left,value)
    else:
        return search(rootNode.right,value)

""" Deletion """

def min_value(bstNode):
    curNode = bstNode

    while curNode.left:
        curNode = curNode.left
    return curNode

def max_value(bstNode):
    curNode = bstNode

    while curNode.right:
        curNode = curNode.right
    return curNode

# def deleteNode(rootNode,nodeValue):
#     if not rootNode:
#         return rootNode
#     if nodeValue < rootNode.data:
#         rootNode.left = deleteNode(rootNode.left,nodeValue)
#     elif nodeValue > rootNode.data:
#         rootNode.right = deleteNode(rootNode.right,nodeValue)
#     else:
#         if rootNode.left is None:
#             tempNode = rootNode.right
#             rootNode = None
#             return tempNode
#         if rootNode.right is None:
#             tempNode = rootNode.left
#             rootNode = None
#             return tempNode
#
#         tempNode = min_value(rootNode.right)
#         rootNode.data = tempNode.data
#         rootNode.right = deleteNode(rootNode.right,tempNode.data)
#     return rootNode

def deleteNode(root,val):
    if not root:
        return root

    # iteration for reaching the exact node
    if val < root.data:
        root.left = deleteNode(root.left,val)
    elif val > root.data:
        root.right = deleteNode(root.right,val)
    else:
        # if the would be deleted node has 1 or less child
        if root.left is None:
            tempNode = root.right
            root = None
            return tempNode
        if root.right is None:
            tempNode = root.left
            root = None
            return tempNode
        # if the would be deleted node has both children
        tempNode = min_value(root.right)
        root.data = tempNode.data
        root.right = deleteNode(root.right,tempNode.data)
    return root




bst = BST(None)
insert(bst,70)
insert(bst,50)
insert(bst,90)
insert(bst,60)
insert(bst,80)
insert(bst,100)
#insert(bst,20)
insert(bst,40)
insert(bst,35)
insert(bst,50)
insert(bst,95)
insert(bst,105)
insert(bst,2)
insert(bst,45)





#preOrderTraverse(bst)
#inOrderTraverse(bst)
#postOrderTraverse(bst)

#levelOrderTraverse(bst)

#print(search(bst,10))

#print(min_value(bst))

deleteNode(bst,2)
print('---------')
levelOrderTraverse(bst)
#print(max_value(bst))
#inOrderTraverse(bst)