class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique=set(word)
        count=0
        for i in unique:
            if i.islower(): 
                if i.upper() in unique:
                    if word.rindex(i) < word.index(i.upper()):
                        count += 1
        return count