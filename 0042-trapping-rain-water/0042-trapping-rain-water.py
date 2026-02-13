# 2 pointers

# Water at an index is limited by the shorter of the best walls on left and right.

# With two pointers, if height[left] < height[right], the left side is the limiting wall, so we can safely compute using left_max (and vice-versa for the right).

# Algorithm

# Set left = 0, right = n - 1, left_max = 0, right_max = 0, ans = 0

# While left < right:

# If height[left] < height[right]:

# If height[left] >= left_max, update left_max

# Else add left_max - height[left] to ans

# Move left += 1

# Else:

# If height[right] >= right_max, update right_max

# Else add right_max - height[right] to ans

# Move right -= 1

# Return ans

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans
        
# Time complexity: O(n)