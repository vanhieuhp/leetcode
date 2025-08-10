from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

def build_binary_tree(arr):
    """
        builds a binary tree from a level-order array list
    """
    if not arr:
        return None

    nodes = []
    for val in arr:
        if val is not None:
            node = TreeNode(val)
        else:
            node = None

        nodes.append(node)

    for i in range(len(arr)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(arr):
                nodes[i].left = nodes[left_index]
            if right_index < len(arr):
                nodes[i].right = nodes[right_index]

    return nodes[0]

def print_tree(node, level=0, label="Root:"):
    """Prints the binary tree structure starting from a given node."""
    if node is not None:
        print("   " * level + label + f" {node.val}")
        print_tree(node.left, level + 1, "L---")
        print_tree(node.right, level + 1, "R---")