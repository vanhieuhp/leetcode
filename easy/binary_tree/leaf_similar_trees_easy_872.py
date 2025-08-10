from utils.binary_tree_utils import build_binary_tree, print_tree, TreeNode
from typing import Optional


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_val(root):
            if root is None:
                return []

            if root.left is None and root.right is None:
                return [root.val]

            leaf_right = get_leaf_val(root.right)
            leaf_left = get_leaf_val(root.left)

            return [] + leaf_left + leaf_right

        leaf_1 = get_leaf_val(root1)
        leaf_2 = get_leaf_val(root2)
        print(leaf_1)
        print(leaf_2)
        return leaf_1 == leaf_2

root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

tree_1 = build_binary_tree(root1)
tree_2 = build_binary_tree(root2)

res = Solution().leafSimilar(tree_1, tree_2)
print(res)