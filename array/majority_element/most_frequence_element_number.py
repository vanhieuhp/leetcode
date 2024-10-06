"""
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.
Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
"""
def mostFrequentEven(nums):
    temp = {}
    result = -1
    temp[result] = -1
    for i in nums:
        if i % 2 == 1:
            continue
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1

        if temp[i] == temp[result]:
            result = min(i, result)
        elif temp[i] > temp[result]:
            result = i
    return result

nums = [0, 1, 2, 2, 4, 4, 1]
print(mostFrequentEven(nums))