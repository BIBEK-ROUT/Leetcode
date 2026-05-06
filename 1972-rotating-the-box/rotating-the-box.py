class Solution(object):
    def rotateTheBox(self, boxGrid):
        n = len(boxGrid[0])
        m = len(boxGrid)
        lis = [[None]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                lis[i][j] = boxGrid[j][i]
        for row in lis:
            row.reverse()
        for j in range(m):
            empty = n - 1  
            for i in range(n-1, -1, -1):
                if lis[i][j] == '*':
                    empty = i - 1  
                elif lis[i][j] == '#':
                    lis[i][j] = '.'
                    lis[empty][j] = '#'
                    empty -= 1
        return lis