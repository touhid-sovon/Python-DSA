
'''
graph can be represented in 3 ways
1. Matrix
2. Adjacency Matrix
3. Adjacency List
'''

# adjacency graph representation
class graphNode:
    def __init__(self,val):
        self.val = val
        self.neighbour = []

