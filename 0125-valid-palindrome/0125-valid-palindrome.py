class Solution:
    def isPalindrome(self, s: str) -> bool:
        buf = ""
        s = s.lower()
        l = 0
        r = len(s)-1
        
        # for c in s:
        #     if ord(c) in range(97,123) or ord(c) in range(48,58):
        #         buf += c 
        # return buf == ''.join(reversed(buf))
        
        while(l < r):
            if s[l] == s[r] and s[l].isalnum() and s[r].isalnum():
                l += 1
                r -= 1
            
            elif s[l] != s[r] and s[l].isalnum() and s[r].isalnum():
                return False
            
            elif not s[l].isalnum():
                while(not s[l].isalnum() and l<r):
                    l += 1
                    
            else:
                while(not s[r].isalnum() and l<r):
                    r -= 1
                    
        return True
            
        