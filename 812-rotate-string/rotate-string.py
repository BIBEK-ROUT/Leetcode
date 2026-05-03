class Solution(object):
    def rotateString(self,s, goal):        
        if(s==goal):
            return True
        if(len(s)!=len(goal)):
            return False
        if(sorted(s)!=sorted(goal)):
            return False
        st=list(s)    
        for i in range(len(s)):
            st=st[1:]+st[0:1]
            if(("".join(st))==goal):
                return True
        return False        