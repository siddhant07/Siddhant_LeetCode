class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1map = {}
        l, r = 0, 0
        for c in s1:
            s1map[c] = 1 + s1map.get(c, 0)
        s1map = sorted(s1map.items())
        s2map = {}
        print(s1map)
        while r < len(s1):
            s2map[s2[r]] = 1 + s2map.get(s2[r], 0)
            r+=1
        
        while r < len(s2):
            if s1map == sorted(s2map.items()):
                return True
             
            s2map[s2[r]] = 1 + s2map.get(s2[r], 0)
            r += 1
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                s2map.pop(s2[l])
            l += 1
            print(sorted(s2map.items()))
            
        if s1map == sorted(s2map.items()):
                return True
        return False