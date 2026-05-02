class Solution(object):
    def rotatedDigits(self, n):
        count=0
        for i in range(1,n+1):
            st=str(i)
            if ('3' in st or '4' in st or '7' in st):
                continue
            if (i==0 or i==1 or i==8 or i==3 or i==4 or i==7):
                continue
            elif ('0' in st or '1' in st or '8' in st):
                if(len(st)!=(st.count('0')+st.count('1')+st.count('8'))):
                    if ('3' in st or '4' in st or '7' in st):
                        continue
                    else:
                        count+=1            
            else:
                count+=1
        return count