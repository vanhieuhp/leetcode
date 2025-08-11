from collections import deque, defaultdict

from utils.binary_tree_utils import TreeNode
from utils.binary_tree_utils import build_binary_tree
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 # basecase: one way to have sum=0

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            count = prefix_sums[curr_sum - targetSum] # path ending here

            prefix_sums[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix_sums[curr_sum] -= 1

            return count

        return dfs(root, 0)


root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
targetSum = 8
binary_tree = build_binary_tree(root)
res = Solution().pathSum(binary_tree, targetSum)
print(res)
