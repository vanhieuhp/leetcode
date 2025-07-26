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
        for i in range(len(s) - 1):
            if value_set[s[i]] < value_set[s[i + 1]]:
                value -= value_set[s[i]]
            else:
                value += value_set[s[i]]

        return value + value_set[s[-1]]

    def romanToInt2(self, s: str) -> int:
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

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        for i in range(len(s)):
            value += value_set[s[i]]

        return value

s = "MCMXCIV"
# value from 1 - 3999
print(Solution().romanToInt2(s))
