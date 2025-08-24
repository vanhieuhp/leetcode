# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pick = 2
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            middle = (right + left) // 2
            res = guess(middle)

            if res == -1:
                right = middle - 1
            elif res == 1:
                left = middle + 1
            else:
                return middle

n = 2
pick = 6
res = Solution().guessNumber(n)
print(res)