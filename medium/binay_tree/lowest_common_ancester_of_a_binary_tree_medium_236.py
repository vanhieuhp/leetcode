from utils.binary_tree_utils import TreeNode
from utils.binary_tree_utils import build_binary_tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

            # If root is p or q, then root is part of the answer
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return non-null, this is the LCA
        if left and right:
            return root

        # Else return the non-null side
        return left if left else right
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 4

res = Solution().lowestCommonAncestor(build_binary_tree(root), TreeNode(p), TreeNode(q))
print(res)
