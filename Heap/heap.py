class TreeNode:
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def arrayToTree(array:list):
    if not array:
        return
    root = TreeNode(array[0])

    i = 1
    n = len(array)
    queue = [root]

    while i < n:
        current = queue.pop(0)

        if i < n and array[i] is not None:
            current.left = TreeNode(array[i])
            queue.append(current.left)
        i += 1

        if i < n and array[i] is not None:
            current.right = TreeNode(array[i])
            queue.append(current.right)

    return root

def heapifyMax(array,n,i):
    largest = i
    left = 2*i
    right = 2*i + 1

    if left < n and array[i] < array[left]:
        largest = left
    if right < n and array[i] < array[right]:
        largest = right

    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapifyMax(array,n,largest)

def heapifyMin(array,n,i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and array[i] > array[left]:
        smallest = left
    if right < n and array[i] > array[right]:
        smallest = right

    if smallest != i:
        array[i],array[smallest] = array[smallest], array[i]
        heapifyMin(array,n,smallest)


def insert(array,newNode):
    size = len(array)
    print(size)
    if size == 0:
        array.append(newNode)
    else:
        array.append(newNode)
        for i in range((size//2)-1,-1,-1):
            heapifyMax(array,size,i)


def deleteNode(array,node):
    size = len(array)
    for i in range(0,size):
        if array[i] == node:
            break

    array[-1],array[i] = array[i],array[-1]
    array.remove(node)

    for i in range((len(array)//2)-1,-1,-1):
        heapifyMax(array,len(array),i)

arr1 = [100,7, 3,88, 14, 33, 22, 18]

insert(arr1,200)
insert(arr1,10)

print(arr1)







