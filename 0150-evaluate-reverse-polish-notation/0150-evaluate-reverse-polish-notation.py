import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv}
        
        for i in tokens:
            if i in ops:
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(int(ops[i](b,a)))
            else:
                stack.append(int(i))
                
        return stack[-1] if stack else 0
                