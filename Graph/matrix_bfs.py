'''

Matrix BFS:
Question: Find the length of the shortest path from top left to bottom right of a matrix
grid = [
    0 0 0 0
    1 1 0 0
    0 0 0 1
    0 1 0 0
]

'''


def bfs(graph):
    Row, Column = len(graph), len(graph[0])

    visited = set()
    queue = []

    queue.append((0, 0))
    visited.add((0, 0))

    length = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.pop(0)
            if r == Row - 1 and c == Column - 1:
                return length

            neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbours:
                t_r, t_c = r + dr, c + dc  # t_r = traversing_row and t_c = traversing_column
                if min(t_r, t_c) < 0 or t_r == Row or t_c == Column or (
                        t_r, t_c) in visited or graph[t_r][t_c] == 1:
                    continue
                queue.append((t_r, c + dc))
                visited.add((t_r, c + dc))

        length += 1


grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

print(bfs(grid))


# again

def bfs2(graph):
    Row , Column = len(graph), len(graph[0])
    visited = set()
    queue = []
    visited.add((0,0))
    queue.append((0,0))
    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.pop(0)
            if r == Row - 1 and c == Column - 1:
                return length

            neighbours = [[0,1],[0,-1],[1,0],[-1,0]]

            for dr, dc in neighbours:
                t_r = r + dr  # traversing_row
                t_c = c + dc  # traversing_column
                if min(t_r,t_c) < 0 or t_r == Row or t_c == Column or (
                    t_r, t_c) in visited or graph[t_r][t_c] == 1:
                    continue
                visited.add((t_r,t_c))
                queue.append((t_r,t_c))

        length += 1

print(bfs2(grid))