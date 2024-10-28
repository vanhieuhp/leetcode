from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for s in strs:
            item = list(s)
            item.sort()
            key = "".join(item)
            if key not in temp:
                temp[key] = [s]
            else:
                temp[key].append(s)

        return list(temp.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(Solution().groupAnagrams(strs))
