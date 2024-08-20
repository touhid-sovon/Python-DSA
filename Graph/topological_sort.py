# geeks for geeks code
'''
Algorithm:
    1. Create a graph with n vertices and m-directed edges.
    2. Initialize a stack and a visited array of size n.
    3. For each unvisited vertex in the graph, do the following:
        i.   Call the DFS function with the vertex as the parameter.
        ii.  In the DFS function, mark the vertex as visited and recursively
             call the DFS function for all unvisited neighbors of the vertex.
        iii. Once all the neighbors have been visited, push the vertex onto the stack.
    4. After all, vertices have been visited, pop elements from the stack
       and append them to the output list until the stack is empty.
    5. The resulting list is the topologically sorted order of the graph.
'''
def topologicalSortUtil(v,adjList,visited,stack):
    visited[v] = True

    for i in adjList[v]:
        if not visited[i]:
            topologicalSortUtil(i,adjList,visited, stack)

    stack.append(v)

def topologicalSort(adjList,V):
    stack = []
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i,adjList,visited,stack)
    while stack:
        print(stack.pop(), end=" ")


if __name__ == "__main__":
    # vertices
    V = 4
    edges = [[0,1],[1,2],[3,1],[3,2]]
    #edges = [["A","C"],["C","D"],["C","D"],["D","F"],["F","G"],["E","F"],["B","C"],["B","F"]]
    # graph represenation of an adjacency list
    adjList = [[] for _ in range(V)]

    #print(adjList)

    for i in edges:
        adjList[i[0]].append(i[1])
    print(adjList)
    # the detailed version of the upper code
    '''
    # Iterate over each edge in the edges list
    for i in edges:
        # Extract the source vertex (i[0]) from the current edge
        source_vertex = i[0]

        # Extract the destination vertex (i[1]) from the current edge
        destination_vertex = i[1]

        # Access the adjacency list for the source vertex
        neighbors_of_source = adjList[source_vertex]

        # Append the destination vertex to the list of neighbors for the source vertex
        neighbors_of_source.append(destination_vertex)
    '''

    # dictionary reprentation
    # adjdict = {}
    # for src,dst in edges:
    #     if src not in adjdict:
    #         adjdict[src] = []
    #     if dst not in adjdict:
    #         adjdict[dst] = []
    #     adjdict[src].append(dst)
    # print(adjdict)

    #topologicalSort(adjList,V)





