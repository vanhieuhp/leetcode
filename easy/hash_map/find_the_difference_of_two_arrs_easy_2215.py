from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # res = []
        #
        # arr_1 = []
        # arr_2 = []
        #
        # dict_1 = dict()
        # dict_2 = dict()
        #
        # for i in range(len(nums1)):
        #     dict_1[nums1[i]] = 1
        #
        # for i in range(len(nums2)):
        #     if nums2[i] not in dict_1:
        #         dict_2[nums2[i]] = 1
        #     else:
        #         dict_1[nums2[i]] = -1
        #
        # for k,v in dict_1.items():
        #     if v == 1:
        #         arr_1.append(k)
        #
        # res.append(arr_1)
        # res.append(list(dict_2.keys()))
        # return res

        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

res = Solution().findDifference(nums1, nums2)
print(res)