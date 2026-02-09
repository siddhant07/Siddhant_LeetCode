class Solution:
    def defangIPaddr(self, address: str) -> str:
        s= ""
        for c in address:
            if c == ".":
                s += "[.]"
            else:
                s += c
        return s
        