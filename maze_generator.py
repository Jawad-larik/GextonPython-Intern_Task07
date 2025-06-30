# maze_generator.py
import random

def generate_maze_with_path(rows, cols):
    # Initialize maze with all walls
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def carve_path(r, c):
        # DFS-based maze carving
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr * 2, c + dc * 2
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1:
                maze[r + dr][c + dc] = 0  # Carve in-between wall
                maze[nr][nc] = 0
                carve_path(nr, nc)

    # Start from (0,0) and carve the maze
    maze[0][0] = 0
    carve_path(0, 0)
    maze[rows - 1][cols - 1] = 0  # Ensure goal is reachable

    # Find a valid path using DFS for path rendering
    path = []
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or visited[r][c] or maze[r][c] == 1:
            return False
        path.append((r, c))
        visited[r][c] = True

        if [r, c] == [rows - 1, cols - 1]:
            return True

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(r + dr, c + dc):
                return True

        path.pop()  # Backtrack if no path forward
        return False

    dfs(0, 0)
    return maze, path