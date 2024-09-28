def removeElement(nums, val):
    if not nums:
        return 0
    k = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Test the function
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print(f"Number of elements not equal to {val}: {k}")
print(f"Modified array: {nums[:k]}")

# Another test case
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = removeElement(nums2, val2)
print(f"\nNumber of elements not equal to {val2}: {k2}")
print(f"Modified array: {nums2[:k2]}")