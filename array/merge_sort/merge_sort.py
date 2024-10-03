def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i = len(nums1) - 1
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[i] = nums1[m - 1]
            m -= 1
        else:
            nums1[i] = nums2[n - 1]
            n -= 1
        i -= 1

    while m > 0:
        nums1[i] = nums1[m - 1]
        i -= 1
        m -= 1

    while n > 0:
        nums1[i] = nums2[n - 1]
        i -= 1
        n -= 1

    print(nums1)
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
# print(result)
