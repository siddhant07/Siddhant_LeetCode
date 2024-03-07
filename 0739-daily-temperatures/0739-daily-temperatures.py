class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                idx, tempVal = stack.pop()
                answer[idx] = i - idx
            stack.append([i, val])
            
            
        return answer
            
        