class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        p=moves.count('L')
        q=moves.count('R')
        dis=0
        if p<q:
            for i in moves:
                if i=='_' or i=='R':
                    dis=dis+1
                else:
                    dis=dis-1
        elif p>q:
            for i in moves:
                if i=='_' or i=='L':
                    dis=dis-1
                else:
                    dis=dis+1
        else:
            for i in moves:
                if i=='_' or i=='R':
                    dis=dis+1
                else:
                    dis=dis-1
        return abs(dis)       