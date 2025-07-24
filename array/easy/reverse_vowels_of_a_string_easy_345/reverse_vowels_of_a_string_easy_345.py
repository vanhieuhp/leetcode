class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s_arr = list(s)
        index = []

        for i in range(len(s_arr)):
            if s_arr[i].lower() in vowels:
                index.append(i)

        i, j = 0, len(index) - 1
        while i < j:
            s_arr[index[i]], s_arr[index[j]] = s_arr[index[j]], s_arr[index[i]]
            i += 1
            j -= 1
        return "".join(s_arr)


s = "leetcode"
result = Solution().reverseVowels(s)

print(result)
