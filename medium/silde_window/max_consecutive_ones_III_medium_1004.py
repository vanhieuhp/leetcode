from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # zero_index = []
        # count = 0
        # index = 0
        # while k > 0 and index < len(nums):
        #     if nums[index] != 1:
        #         k = k - 1
        #         zero_index.append(index)
        #
        #     index = index + 1
        #     count = count + 1
        #
        # res = count
        #
        # for i in range(index, len(nums)):
        #     if nums[i] == 1:
        #         count = count + 1
        #     elif len(zero_index) == 0:
        #         count = 0
        #     else:
        #         count = i - zero_index[0]
        #         zero_index.append(i)
        #         zero_index.pop(0)
        #
        #     res = max(res, count)
        #
        # return res

        left = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 0
res = Solution().longestOnes(nums, k)
print(res)
