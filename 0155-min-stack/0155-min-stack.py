class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minVal[-1] if self.minVal else val)
        self.minVal.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()