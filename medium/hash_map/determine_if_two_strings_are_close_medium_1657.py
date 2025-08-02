from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if set(word1) != set(word2):
            return False
        
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

word1 = "uau" # z -> zz = 2 (1,2,2,2)
word2 = "ssx" # z -> zzz = 3 (1,1,2,3)
res = Solution().closeStrings(word1, word2)
print(res)