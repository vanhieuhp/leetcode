class Solution:
    def isPalindrome(self, s: str) -> bool:

        processed = ''.join([c for c in s if c.isalnum()])

        # convert to lower string
        processed = processed.lower()
        print(processed)

        return processed == processed[::-1]


s = "A man, a plan, a canal: Panama"

print(Solution().isPalindrome(s))

