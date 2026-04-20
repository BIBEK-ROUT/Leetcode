class Solution(object):
    def maxDistance(self, colors):
        self.colors=colors
        uni=set(self.colors)
        num=[]
        for i in uni:
            j=len(self.colors)-1
            while j>=0:
                if(i!=self.colors[j]):
                    num.append(abs(self.colors.index(i)-j))
                    break
                else:
                    j=j-1
        return max(num)
        