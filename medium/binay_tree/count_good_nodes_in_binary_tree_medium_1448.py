from utils.binary_tree_utils import TreeNode
from utils.binary_tree_utils import build_binary_tree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, max_val):
            if not node:
                return 0

            count = 1 if node.val >= max(max_val, node.val) else 0

            max_val = max(max_val, node.val)

            count += traverse(node.left, max_val)
            count += traverse(node.right, max_val)

            return count

        return traverse(root, root.val)


root = [3, 1, 4, 3, None, 1, 5]
binary_tree = build_binary_tree(root)
res = Solution().goodNodes(binary_tree)
print(res)
