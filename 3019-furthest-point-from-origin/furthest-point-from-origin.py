class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        p=moves.count('L')
        q=moves.count('R')
        U=moves.count('_')
        return abs(p-q) + U