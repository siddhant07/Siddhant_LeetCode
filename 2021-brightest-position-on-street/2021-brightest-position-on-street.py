from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        lo = float('inf')
        hi = float('-inf')

        for c, r in lights:
            lo = min(lo, c - r)
            hi = max(hi, c + r)

        off = lo
        B = {}

        for c, r in lights:
            start = c - r - off
            end = c + r - off + 1
            B[start] = B.get(start, 0) + 1
            B[end] = B.get(end, 0) - 1

        curr = 0
        max_val = 0
        res = off

        for k in sorted(B):
            curr += B[k]
            if curr > max_val:
                max_val = curr
                res = k + off

        return res