class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = set('aeiou')
        count = sum(1 for c in s[:k] if c in vowels)

        if count == k:
            return count

        max_count = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            
            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

            if max_count == k:
                return max_count

        return max_count

s = "tryhard"
k = 4

result = Solution().maxVowels(s, k)
print(result)