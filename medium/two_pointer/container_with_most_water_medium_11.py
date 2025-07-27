from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right =0, len(height) - 1
        result = 0
        while left < right:
            w_c = right - left
            r_c = min(height[left], height[right])
            containter = w_c * r_c
                
            if result < containter:
                result = containter

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = Solution().maxArea(height)

print(result)