from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = []
        if strs and len(strs) > 0:
            strs = sorted(strs)
            first, last = strs[0], strs[-1]
            for i in range(len(first)):
                if len(last) > i and last[i] == first[i]:
                    longest_pre.append(last[i])
                else:
                    return "".join(longest_pre)
        return "".join(longest_pre)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


# strs = ["flower", "flow", "flight"]
strs = ["ab", "a"]
print(Solution().longestCommonPrefix2(strs))  # "fl"
