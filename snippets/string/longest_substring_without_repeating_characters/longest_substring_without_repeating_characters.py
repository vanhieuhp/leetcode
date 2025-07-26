class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)
        left = 0
        max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length
# s = "abcabcbb"
s = "pwwkew"
# s = "bbbbb"
# s = " "
# s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
