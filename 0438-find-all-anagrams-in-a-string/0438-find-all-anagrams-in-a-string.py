from collections import Counter

# Build reference counter pCount for string p.

# Move the sliding window along the string s:

#    Recompute sliding window counter sCount at each step by adding one letter on the right and      removing one letter on the left.

#       If sCount == pCount, update the output list.

# Return output list.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []

        # sliding window on the string s
        for i in range(ns):
            # Add one more letter 
            # on the right side of the window
            s_count[s[i]] += 1

            # Remove one letter 
            # from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            # Compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output
       
       
        # O(Ns) -> Ns is length of s