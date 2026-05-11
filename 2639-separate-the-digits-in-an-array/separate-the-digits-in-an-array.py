class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lis=[]
        for i in nums:
            lis1=str(i)
            lis=lis+list(lis1)
        # olis=lis[::-1]
        olis1=[int(x) for x in lis]
        return olis1
            
        