class Solution(object):
    def maxDistance(self, nums1, nums2):
        self.nums1=nums1
        self.nums2=nums2
        num=0
        i=0
        j=0
        while i <len(self.nums1) and j<len(self.nums2):
            if(self.nums1[i]<=self.nums2[j]):
                num=max(num,j-i)
                j+=1
            else:
                i+=1
        return num
        