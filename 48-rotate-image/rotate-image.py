class Solution(object):
    def rotate(self, matrix):
        l = len(matrix)
        for i in range(l):
            for j in range(i + 1, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(l):
            matrix[i].reverse()   
        return matrix