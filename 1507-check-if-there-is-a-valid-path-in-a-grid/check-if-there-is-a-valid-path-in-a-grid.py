class Solution(object):
    def hasValidPath(self, grid):
        direct = {
            1: [(0, 1), (0, -1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        rows = len(grid)
        cols = len(grid[0])
        stack = [(0, 0)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if x == rows - 1 and y == cols - 1:
                return True
            for dx, dy in direct[grid[x][y]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    back = (-dx, -dy)
                    if back in direct[grid[nx][ny]]:
                        stack.append((nx, ny))
        return False