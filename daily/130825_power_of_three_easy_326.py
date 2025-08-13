
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        val = 1
        i = 0
        
        while val < n:
            val = 3 ** i
            if val == n:
                return True

            i += 1

        return False    

n = 27
res = Solution().isPowerOfThree(n)
print(res)