class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        current_number = 0
        current_string = 0
        count_stack = []
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == "]":
                string_stack.append(current_string)
                count_stack.append(current_number)
                current_number = 0
                current_string = ""
            elif char == "]":
                repeat_times = count_stack.pop()
                prev_string = string_stack.pop()
                current_string = prev_string + current_string * repeat_times
            else:
                current_string += char
        return current_string

s = "3[a2[c]]" # abcabccdcdcdef
res = Solution().decodeString(s)
print(res)git