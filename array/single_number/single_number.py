def singleNumber(nums):
    res = 0 # n ^ 0 = n
    for n in nums:
        res = n ^ res
    return res

nums = [2, 3, 1, 2, 3]
single_num = singleNumber(nums)
print(single_num)