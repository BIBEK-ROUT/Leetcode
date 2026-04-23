class Solution(object):
    def twoEditWords(self, queries, dictionary):
        length=len(queries[0])
        lis=[]
        for i in queries:
            for j in dictionary:
                p=0
                count=0
                while p<length:
                    if i[p]!=j[p]:
                        count+=1
                        if count>2:
                            break
                    p=p+1
                if count<=2:
                    lis.append(i)
                    break
        return lis
