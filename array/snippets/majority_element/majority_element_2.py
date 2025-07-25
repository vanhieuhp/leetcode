"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

def majorityElement(nums):
    l = len(nums) // 3 + 1
    temp = {}
    result = []
    for i in nums:
        if i not in temp:
            temp[i] = l - 1
        else:
            temp[i] = temp[i] - 1
        if temp[i] == 0:
            result.append(i)
    return result


# nums = [3, 2, 3]
nums = [1,2]
# nums = [1]
print(majorityElement(nums))