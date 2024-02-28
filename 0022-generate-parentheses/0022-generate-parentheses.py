class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openc, closec):
            if openc == closec == n:
                res.append("".join(stack))
                return
                
            if openc < n:
                stack.append("(")
                backtrack(openc + 1, closec)
                stack.pop()
                
                
            if closec < openc:
                stack.append(")")
                backtrack(openc, closec + 1)
                stack.pop()
                
        backtrack(0,0)
        return res
                
        
        
        