def majorityElement(nums):
    l = len(nums) // 2 + 1
    temp = {}
    for i in nums:
        if i not in temp:
            temp[i] = l - 1
        else:
            temp[i] = temp[i] - 1
        if temp[i] == 0:
            return i


# nums = [3, 2, 3]
nums = [1]
print(majorityElement(nums))