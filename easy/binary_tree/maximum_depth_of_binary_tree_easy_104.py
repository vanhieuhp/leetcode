from utils.binary_tree_utils import build_binary_tree, print_tree, TreeNode

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(node):
            if node is not None:
                left_depth = max_depth(node.left)
                right_depth = max_depth(node.right)
                return 1 + max(left_depth, right_depth)
            else:
                return 0

        return max_depth(root)


root = [3, 9, 20, None, None, 15, 7]
binary_tree = build_binary_tree(root)
print_tree(binary_tree, level=0)

res = Solution().maxDepth(binary_tree)
print(res)