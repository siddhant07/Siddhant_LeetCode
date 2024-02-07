class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        length = 0
        
        alpha = {}
        
        for r in range(len(s)):
            alpha[s[r]] = 1 + alpha.get(s[r], 0)
            
            while( r - l + 1 - max(alpha.values()) > k ) :
                alpha[s[l]] -= 1
                l += 1            
            length = max(length, r - l + 1)
                
                
        return length
            
        
        
        
        
        
        
        
        
        
        
#         c = k
        
#         while r < len(s):
#             print(s[l], s[r])
#             if s[r] != s[l] and c > 0:
#                 c -= 1
#                 length += 1
#                 print(length, c, " if")
#             elif s[r] != s[l] and c == 0: 
#                 l = r
#                 maxlen = max(maxlen, length)
#                 length = 1
#                 c = k
#                 print(length, c, " elif")
#             else:
#                 length += 1
#             r += 1
#         maxlen = max(maxlen, length)
#         return maxlen

        