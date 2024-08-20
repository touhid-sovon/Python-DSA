def bfs(graph,source):
    queue = [source]
    visit = [source]
    while queue:
        curr = queue.pop(0)
        print(curr)
        for neighbour in graph[curr]:
            if neighbour not in visit:
                queue.append(neighbour)
                visit.append(neighbour)

graph = {
    "A": ["B","C"],
    "B": ["A","D","E"],
    "C": ["A","E"],
    "D": ["B","E","F"],
    "E": ["C","D","F"],
    "F": ["D","E"]
}

#bfs(graph,"A")

def dfs(graph,source):
    stack = [source]
    visit = [source]
    while stack:
        curr = stack.pop()
        print(curr)
        for neighbour in graph[curr]:
            if neighbour not in visit:
                stack.append(neighbour)
                visit.append(neighbour)

dfs(graph,"A")
