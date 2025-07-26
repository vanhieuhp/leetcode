from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        print(chars)
        return write

# chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
result = Solution().compress(chars)
print(result)