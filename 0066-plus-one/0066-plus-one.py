class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1] += 1
            return digits
        n = len(digits)
        for i in range(n):
            idx = n-1-i

            if digits[idx]== 9:
                digits[idx] = 0
            else:
                digits[idx]+=1
                return digits

        return [1]+digits

        