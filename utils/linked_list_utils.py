from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(nums: List) -> Optional[ListNode]:
    root = ListNode(nums[0])
    current = root

    for i in range(1, len(nums)):
        new_node = ListNode(nums[i])
        current.next = new_node
        current = new_node

    return root


def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
