class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding open bracket
        bracket_map = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map:  # If it's a closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:  # If it's an invalid character (though the problem says input is valid)
                return False

        # If the stack is empty, all brackets are matched
        return not stack

s = "[({(())}[()])]"
print(Solution().isValid(s))
