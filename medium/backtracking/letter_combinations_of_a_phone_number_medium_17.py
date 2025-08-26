from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        def backtracking(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                backtracking(index + 1, path + letter)

        backtracking(0, "")

        return result
            

digits = "23"
res = Solution().letterCombinations(digits)
print(res)
