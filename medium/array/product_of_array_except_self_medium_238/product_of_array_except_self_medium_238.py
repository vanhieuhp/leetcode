from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_arr = len(nums)
        answer = [1] * len_arr
        
        for i in range(1,len_arr):
            answer[i] = answer[i - 1] * nums[i-1]
        
        suffix = 1
        for i in range(len_arr - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
    
nums = [1,2,3,4]
answer = Solution().productExceptSelf(nums)
print(answer)