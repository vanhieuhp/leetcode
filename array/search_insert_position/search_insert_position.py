
def searchInsert(nums, target):
    if len(nums) == 0:
        return 0

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

nums = [1, 3, 5, 6]
target = 7

index = searchInsert(nums, target)
print("index: ", index)
