from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if flowerbed[0] == 1:
            i_place = 2
        else:
            i_place = 0

        while i_place < len(flowerbed):
            if flowerbed[i_place] == 1:
                i_place += 2
                continue

            if i_place + 1 < len(flowerbed) and flowerbed[i_place + 1] == 1:
                i_place += 3
                continue

            i_place += 2
            n = n - 1
            if n == 0:
                return True

        return False

flowerbed = [1, 0, 0, 0, 0, 1]
n = 2
result = Solution().canPlaceFlowers(flowerbed, n)
print(result)
