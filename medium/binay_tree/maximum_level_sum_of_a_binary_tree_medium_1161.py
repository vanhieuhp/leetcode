from collections import deque, defaultdict
from utils.binary_tree_utils import TreeNode, build_binary_tree


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_val = root.val
        max_level = 1
        level = 1
        queue = deque([root])

        while queue:
            len_queue = len(queue)

            total = 0
            for i in range(len_queue):
                node = queue.popleft()
                total = total + node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if total > max_val:
                max_level = level
                max_val = total
            level += 1

        return max_level


    def maxLevelSum2(self, root: TreeNode) -> int:
        levels = defaultdict(int)

        def dfs(node, i):
            if not node:
                return
            levels[i] += node.val

            dfs(node.left, i+1)
            dfs(node.right, i+1)    

        dfs(root, 1)
        return max(levels, key=lambda x: levels[x])

# root = [1, 7, 0, 7, -8, None, None]
root = [989, None, 10250, 98693, -89388, None, None, None, -32127]

tree = build_binary_tree(root)
res = Solution().maxLevelSum(tree)
print(res)
