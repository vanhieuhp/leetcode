from collections import deque
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
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        current = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def build_bst(values):
    root = None
    for v in values:
        if v is None:
            continue
        root = insert(root, v)
    return root


def print_tree(node, level=0, label="Root:"):
    """Prints the binary tree structure starting from a given node."""
    if node is not None:
        print("   " * level + label + f" {node.val}")
        print_tree(node.left, level + 1, "L---")
        print_tree(node.right, level + 1, "R---")