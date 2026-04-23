from collections import defaultdict
class Solution(object):
    def distance(self, nums):
        groups = defaultdict(list)   
        for i, num in enumerate(nums):
            groups[num].append(i)
        res = [0] * len(nums)  
        for indices in groups.values():
            n = len(indices) 
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            for i in range(n):
                idx = indices[i]
                left = idx * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - idx * (n - i - 1)
                res[idx] = left + right
        
        return res