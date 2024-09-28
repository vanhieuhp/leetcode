class Solution(object):
    def two_sum(self, nums, target):
        temp_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num in temp_map:
                return temp_map[num], i
            else:
                temp_map[complement] = i

# nums = [2,7,11,15]
# target = 9
# nums = [3,2,4]
# target = 6

nums = [3,3]
target = 6
solution = Solution()
result = solution.two_sum(nums, target)
print(result)