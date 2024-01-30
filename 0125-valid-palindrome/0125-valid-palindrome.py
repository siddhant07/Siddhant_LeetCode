class Solution:
    def isPalindrome(self, s: str) -> bool:
        buf = ""
        s = s.lower()
        
        for c in s:
            if ord(c) in range(97,123) or ord(c) in range(48,58):
                buf += c 
                
        print(buf)
        
        if buf == ''.join(reversed(buf)):
            return True
        