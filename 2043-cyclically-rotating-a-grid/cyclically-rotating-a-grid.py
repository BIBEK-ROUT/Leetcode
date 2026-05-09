class Solution:
    def rotateGrid(self, grid, k):
        r = len(grid)
        c = len(grid[0])
        layers = min(r, c) // 2
        for i in range(layers):
            arr = []
            top = i
            left = i
            bottom = r - i - 1
            right = c - i - 1
            for j in range(left, right + 1):
                arr.append(grid[top][j])
            for j in range(top + 1, bottom):
                arr.append(grid[j][right])
            for j in range(right, left - 1, -1):
                arr.append(grid[bottom][j])
            for j in range(bottom - 1, top, -1):
                arr.append(grid[j][left])
            rotate = k % len(arr)
            arr = arr[rotate:] + arr[:rotate]
            idx = 0
            for j in range(left, right + 1):
                grid[top][j] = arr[idx]
                idx += 1
            for j in range(top + 1, bottom):
                grid[j][right] = arr[idx]
                idx += 1
            for j in range(right, left - 1, -1):
                grid[bottom][j] = arr[idx]
                idx += 1
            for j in range(bottom - 1, top, -1):
                grid[j][left] = arr[idx]
                idx += 1
        return grid