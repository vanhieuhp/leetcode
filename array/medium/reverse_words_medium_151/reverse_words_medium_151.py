class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = s.split(" ")
        result = []

        for i in range(len(s_array) - 1, -1, -1):
            if s_array[i] == "":
                continue
            result.append(s_array[i])

        return " ".join(result)

s = "  hello world  "

result = Solution().reverseWords(s)
print(result)