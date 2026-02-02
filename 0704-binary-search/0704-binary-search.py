class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BinarySearch(low, high):
            mid = (low+high)//2

            if low > high:
                return -1
            
            if nums[mid] == target:
                return mid
            
            if nums[mid]>target:
                return BinarySearch(low, mid - 1)
            else:
                return BinarySearch(mid + 1, high)
            
        return BinarySearch(0, len(nums)-1)
        