class BinaryTreeList:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size

    def insert(self,value):
        if self.lastUsedIndex+1 == self.maxsize:
            return "The list is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "Successful Insertion"

    def search(self,nodeval):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeval:
                return "Found"
        return

    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)

    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])

    def levelOrderTraversal(self):
        if self.lastUsedIndex == 0:
            print("The tree is empty")
            return
        for i in range(1,self.lastUsedIndex+1):
            print(self.customList[i])

    def deepestNode(self):
        return self.customList[self.lastUsedIndex]

    def deleteDeepestNode(self):
        self.customList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1
        return

    def deleteNthNode(self,value):
        if self.lastUsedIndex == 0:
            return "The tree is empty"
        replaceNode = self.deepestNode()
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = replaceNode
                self.deleteDeepestNode()
                return
    def deleteBT(self):
        self.customList = None
        self.lastUsedIndex = 0
        return

newBT = BinaryTreeList(10)

newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")
newBT.insert("Coke")
newBT.insert("Pepsi")

# print(newBT.search("Hot"))

# newBT.preOrderTraversal(1)
#newBT.inOrderTraversal(1)
#newBT.postOrderTraversal(1)

#newBT.levelOrderTraversal()

# print(newBT.deepestNode())
#
# newBT.deleteDeepestNode()

#newBT.deleteNthNode('Tea')

newBT.deleteBT()


newBT.levelOrderTraversal()