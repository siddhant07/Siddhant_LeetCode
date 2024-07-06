class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter=0
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha():
                counter+=1
            if counter>0 and not s[i].isalpha():
                return counter
        
        return counter
        