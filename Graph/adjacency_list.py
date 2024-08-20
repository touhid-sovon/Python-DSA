# can be used a class named gpaghNode or node
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbour = []


# Or using a HashMap or Dictionary
# adjList = {
#     "A": [],
#     "B": []
# }

# given directed edges, create adjacency list
edges = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["E", "F"]]


def createAdjList(edges: list) -> dict:
    adjList = {}

    for src, dst in edges:
        if src not in adjList:
            adjList[src] = []
        if dst not in adjList:
            adjList[dst] = []
        adjList[src].append(dst)
    return adjList

#print(createAdjList(edges))

adjList = createAdjList(edges)

#print(adjList)


# dfs for counting the paths from source to destinationn
# backtracking method

def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for neighbour in adjList[node]:
        count += dfs(neighbour,target,adjList,visit)
    visit.remove(node)

    return count

edges2 = [["A", "B"], ["B", "C"], ["B", "D"], ["C", "D"], ["D", "E"]]
adjList2 = createAdjList(edges2)

#print(dfs("A","E",adjList2,set()))

# bfs : shortest path from source to destination

def bfs(node,target,adjList):
    visit = set()
    queue = []

    visit.add(node)
    queue.append(node)
    length = 0

    while queue:
        for i in range(len(queue)):
            cur_node = queue.pop(0)
            if cur_node == target:
                return length

            for neighbour in adjList[cur_node]:
                if neighbour not in visit:
                    visit.add(neighbour)
                    queue.append(neighbour)
        length += 1
    return length

print(bfs("A","E",adjList2))









