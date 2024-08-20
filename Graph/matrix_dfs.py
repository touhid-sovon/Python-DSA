'''
Ques: Count the unique paths from top left to bottom right. A single path
may only move along 0's and can't visit the same cell more than once.

The grid or matrix is:

0 0 0 0
1 1 0 0
0 0 0 1
0 1 0 0

'''


def dfs(grid, r, c, visited: set) -> int:
    Row, Column = len(grid), len(grid[0])

    if min(r, c) < 0 or r == Row or c == Column or (r, c) in visited or grid[r][c] == 1:
        return 0
    if r == Row - 1 and c == Column - 1:
        return 1

    visited.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visited)
    count += dfs(grid, r - 1, c, visited)
    count += dfs(grid, r, c + 1, visited)
    count += dfs(grid, r, c - 1, visited)

    visited.remove((r, c))

    return count

matrix = [[0,0,0,0],[1,1,0,0],[0,0,0,1],[0,1,0,0]]

#print(dfs(matrix,0,0,set()))


# same code without passing hashmap

def dfs(grid, r, c, visited=None) -> int:
    if visited is None:
        visited = set()  # Create the visited set only once

    Row, Column = len(grid), len(grid[0])

    # Base cases
    if min(r, c) < 0 or r == Row or c == Column or (r, c) in visited or grid[r][c] == 1:
        return 0
    if r == Row - 1 and c == Column - 1:
        return 1

    visited.add((r, c))

    # Explore all four directions
    count = 0
    count += dfs(grid, r + 1, c, visited)
    count += dfs(grid, r - 1, c, visited)
    count += dfs(grid, r, c + 1, visited)
    count += dfs(grid, r, c - 1, visited)

    visited.remove((r, c))  # Backtrack

    return count

# Example usage
grid = [[0,0,0,0],[1,1,0,0],[0,0,0,1],[0,1,0,0]]
print(dfs(grid, 0, 0))  # Should output the number of unique paths
