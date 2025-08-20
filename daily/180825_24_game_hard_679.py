from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]):
        EPSILON = 1e-6

        def backtrack(nums):
            len_n = len(nums)

            if len_n == 1:
                return abs(nums[0] - 24) < EPSILON

            for i in range(len_n):
                for j in range(i + 1, len_n):
                    a, b = nums[i], nums[j]

                    possible = [a + b, a - b, b - a, a * b]

                    if abs(b) > EPSILON:
                        possible.append(a / b)
                    if abs(a) > EPSILON:
                        possible.append(b / a)

                    # build the list after combining a and b
                    next_nums = [nums[k] for k in range(len_n) if k != i and k != j]

                    for val in possible:
                        if backtrack(next_nums + [val]):
                            return True
            return False

        return backtrack([float(x) for x in cards])


# cards = [4, 1, 8, 7]
# res = Solution().judgePoint24(cards)
# print(res)
