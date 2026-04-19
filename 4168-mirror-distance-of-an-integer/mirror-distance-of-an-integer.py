class Solution(object):
    def mirrorDistance(self, n):
        self.n=n
        reversed_num=int(str(self.n)[::-1])
        return abs(reversed_num-self.n)
