class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result=[]
        l=len(nums)
        def calculate(nums):
            sum=[]
            for i in range(l):
                if i==0:
                    sum.append(0)
                else:
                    sum.append(sum[i-1]+nums[i-1])
            return sum
        leftsum=calculate(nums)
        rightsum=calculate(nums[::-1])
        reverse=rightsum[::-1]
        for i in range(l):
            result.append(abs(leftsum[i]-reverse[i]))
        return result


