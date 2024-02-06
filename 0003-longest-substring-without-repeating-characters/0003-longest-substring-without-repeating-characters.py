class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0 , 0
        cur, maxlen = 0, 0
        newList = set()
        
        while r < len(s):
            if s[r] not in newList:
                newList.add(s[r])
                print(s[r] + " if")
                cur += 1
                print(cur)
            else:
                print(s[r] + " else")
                while s[l] != s[r]:
                    newList.remove(s[l])
                    l += 1
                l += 1
                maxlen = max(maxlen, cur)
                print(l, maxlen)
                cur = r - l + 1
            r += 1
            maxlen = max(maxlen, cur)
        return maxlen
            
            