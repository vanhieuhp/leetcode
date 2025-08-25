from typing import List
from collections import deque

class HeapNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
def build_heap(self, arr: List[int]):
    root = HeapNode(arr[0])
    queue = deque([root])
    
    i = 1
    while queue and i < len(arr):
        current = queue.popleft()

        left_node = HeapNode(arr[i])
        left_node.parent = current
        current.left = left_node
        i += 1

        right_node = HeapNode(arr[i])
        right_node.parent = current
        current.right = right_node
        i+=1

    