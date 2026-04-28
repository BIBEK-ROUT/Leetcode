import statistics
class Solution(object):
    def minOperations(self, grid, x):
        lis = [num for row in grid for num in row]
        lis.sort()
        temp = []
        s = lis[0] % x
        medi = statistics.median(lis)
        low_medi = medi - (medi % x) + s
        if low_medi > medi:
            low_medi -= x
        high_medi = low_medi + x
        candidates = [low_medi, high_medi]
        best_medi = min(candidates, key=lambda c: abs(c - medi))
        for i in lis:
            if i % x != s:
                return -1
            else:
                var = abs(best_medi - i) // x
                temp.append(var)
        return int(sum(temp))