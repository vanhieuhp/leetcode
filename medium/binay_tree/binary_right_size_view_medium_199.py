from utils.binary_tree_utils import TreeNode, build_binary_tree
from typing import Optional, List
from collections import deque


class Solution:
    # BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # if it's the last node in this level
                if i == level_size - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res


# root = [1, 2, 3, 4, None, None, None, 5]
root = [1, 2, 3, 4, None, None, None, 5]
res = Solution().rightSideView(build_binary_tree(root))
print(res)
