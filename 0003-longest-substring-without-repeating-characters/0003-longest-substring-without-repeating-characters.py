class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0 , 0
        cur, maxlen = 0, 0
        newList = set()
        
        while r < len(s):
            if s[r] not in newList:
                newList.add(s[r])
                cur += 1
            else:
                while s[l] != s[r]:
                    newList.remove(s[l])
                    l += 1
                l += 1
                maxlen = max(maxlen, cur)
                cur = r - l + 1
            r += 1
            maxlen = max(maxlen, cur)
        return maxlen
            
            