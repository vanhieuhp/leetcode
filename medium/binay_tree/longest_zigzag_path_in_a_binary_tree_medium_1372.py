from utils.binary_tree_utils import TreeNode
from utils.binary_tree_utils import build_binary_tree, print_tree

from typing import Optional


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_size = 0

        def dfs(node, direction, length):
            if not node:
                return

            self.max_size = max(self.max_size, length)

            if direction == "left":
                dfs(node.right, "right", length + 1)
                dfs(node.left, "left", 1)
            else:
                dfs(node.left, "left", length + 1)
                dfs(node.right, "right", 1)

        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)

        return self.max_size

root = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
print_tree(build_binary_tree(root))
# res = Solution().longestZigZag(build_binary_tree(root))
# print(res)