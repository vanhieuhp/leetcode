class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for v in s:
            if v != "*":
                stack.append(v)
            elif v == "*" and stack:
                stack.pop()

        return "".join(stack)
        

s = "leet**cod*e"
res = Solution().removeStars(s)
print(res)