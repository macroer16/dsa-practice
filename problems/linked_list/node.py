"""A node in a singly linked list, plus helpers for building and reading lists in tests."""
from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def from_list(values: list[int]) -> ListNode | None:
    """Build a linked list from a Python list, e.g. [1, 2, 3] -> 1 -> 2 -> 3."""
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: ListNode | None) -> list[int]:
    """Read a linked list back into a Python list."""
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out
