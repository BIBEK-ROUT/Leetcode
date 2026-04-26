class Solution(object):
    def containsCycle(self, grid):
        row = len(grid)
        col = len(grid[0])
        lis = [z for y in grid for z in y]
        s = set(lis)
        temp = []
        for ch in s:
            if lis.count(ch) >= 4:
                temp.append(ch)
        if len(temp) == 0:
            return False
        visited = set()
        def dfs(x, y, px, py, ch):
            visited.add((x, y))
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue
                if grid[nx][ny] != ch:
                    continue
                if nx == px and ny == py:
                    continue
                if (nx, ny) in visited:
                    return True
                if dfs(nx, ny, x, y, ch):
                    return True
            return False
        for i in range(row):
            for j in range(col):
                if (i, j) in visited:
                    continue
                if grid[i][j] not in temp:
                    continue
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True
        return False