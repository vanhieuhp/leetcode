class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            ci = (c & 1)
            ai = (a & 1)
            bi = (b & 1)

            if ci == 0:
                count += (ai + bi)
            else:
                if ai + bi == 0:
                    count += 1
            c >>= 1
            b >>= 1
            a >>= 1
        
        return count

a = 8
b = 3
c = 5

res = Solution().minFlips(a, b, c)
print(res)