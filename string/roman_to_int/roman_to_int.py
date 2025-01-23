class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        value_set = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000   
        }
        summit = 0
        characters = list(s)
        for i in range(0, len(characters)):
            if value_set[characters[i]] >= value_set[characters[summit]]:
                summit = i

        value += value_set[characters[summit]]
        for i in range(summit-1, -1, -1):
            value += value_set[i]

        for i in range(summit+1, len(characters)):
            value += value_set[characters[i]]
        return value

s = "MCMXCIV"

print(Solution().romanToInt(s))