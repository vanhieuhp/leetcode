from typing import Optional
from utils.binary_tree_utils import TreeNode, build_bst, print_tree


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        
        return None

root = [4, 2, 7, 1, 3]
val1 = 2
tree = build_bst(root)
res = Solution().searchBST(tree, val1)
print(res)

print_tree(build_bst(root))