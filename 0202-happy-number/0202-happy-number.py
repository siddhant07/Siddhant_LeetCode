class Solution:
    def isHappy(self, n: int) -> bool:
        cycle_members = set()
        def get_next(number):
            total_sum = 0
            while number > 0:
                number,digit = divmod(number,10)
                total_sum += digit**2
            return total_sum
        
        while n!=1 and n not in cycle_members:
            cycle_members.add(n)
            n = get_next(n)
        return n == 1

        

        