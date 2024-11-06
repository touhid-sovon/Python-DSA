'''
Backtracking: It is normally based on DFS algorithm. It is recursive and also it's bruteforce method. We need to go
to every solution and backtrack if there is a contradiction and then find the solution.
'''

''' Questoion:

Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeroes.
            4
           /  \
          0    1
           \  / \
           7 2  0
'''

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def canReachLeaf(root):
    if not root or root.val == 0:
        return False

    if not root.left or not root.right:
        return True

    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True

    return False

root = TreeNode(4,TreeNode(0,None,TreeNode(7)),TreeNode(1,TreeNode(2),TreeNode(0)))

print(canReachLeaf(root))


