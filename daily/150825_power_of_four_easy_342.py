import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = 0
        i = 0
        while power <= n:
            power = math.pow(4, i)
            if power == n:
                return True
            i += 1
            
        return False

    def isPowerOfFourBinary(self, n: int) -> bool:


n = 0
res = Solution().isPowerOfFour(n)
print(res)