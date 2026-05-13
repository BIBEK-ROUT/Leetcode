class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        f = 0
        for i in range(n):
            f += i * nums[i]
        max_val = f
        for k in range(1, n):
            f = f + total_sum - n * nums[-k]
            max_val = max(max_val, f)
        return max_val