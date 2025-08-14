from typing import Optional
from utils.binary_tree_utils import TreeNode, build_bst, print_tree

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # node to delete found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_node = self.findMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node


root = [3]
key = 3

tree_node = build_bst(root)
res = Solution().deleteNode(tree_node, key)
print_tree(res)