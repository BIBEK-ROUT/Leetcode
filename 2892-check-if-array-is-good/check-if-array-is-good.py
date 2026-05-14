class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        lis=[x for x in range(1,n)]
        if len(nums)!=n+1:
            return False
        for i in lis:
            if i not in nums and nums.count(i)!=1:
                return False
        if nums.count(n)!=2:
            return False
        return True