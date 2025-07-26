from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst: [int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def length_recursive(head):
    if head is None:
        return 0
    else:
        return 1 + length_recursive(head.next)

def display(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print()
