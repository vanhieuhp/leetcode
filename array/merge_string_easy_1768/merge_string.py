class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        len1, len2 = len(word1), len(word2)
        i = 0

        while i < len1 and i < len2:
            result.append(word1[i])
            result.append(word2[i])
            i += 1

        if i < len1:
            result.append(word1[i:])
        elif i < len2:
            result.append(word2[i:])

        return "".join(result)

result = Solution().mergeAlternately(word1="abc", word2="abc")
print(result)