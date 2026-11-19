"""S05 STUDENT STARTER — intentionally incomplete, not an official answer key.

Teaching-only contract:
    put(key: int, value) -> None    # insert or update
    get(key: int) -> value          # KeyError if missing
    delete(key: int) -> None        # KeyError if missing
    contains(key: int) -> bool
    len(table) -> int

Do not use a dict as the internal storage of your three implementations.
The exact graded-assignment API and rules remain pending institutional confirmation.
"""
from dataclasses import dataclass
from typing import Any, Optional


class ArraySymbolTable:
    """Unsorted array/list of (key, value) pairs; enforce unique keys."""

    def __init__(self):
        self.entries = []  # TODO: define and maintain representation invariant

    def put(self, key: int, value: Any) -> None:
        # TODO: search for existing key; update or insert without duplicates
        raise NotImplementedError("Student task: array put")

    def get(self, key: int) -> Any:
        # TODO: scan and return the value or raise KeyError
        raise NotImplementedError("Student task: array get")

    def delete(self, key: int) -> None:
        # TODO: find, remove, preserve unrelated entries or raise KeyError
        raise NotImplementedError("Student task: array delete")

    def contains(self, key: int) -> bool:
        # TODO: test membership without confusing stored None with missing
        raise NotImplementedError("Student task: array contains")

    def __len__(self) -> int:
        # TODO: unique key count
        raise NotImplementedError("Student task: array size")


@dataclass
class ListNode:
    key: int
    value: Any
    next: Optional['ListNode'] = None


class LinkedSymbolTable:
    """Singly linked chain. Do not lose the remaining chain during deletion."""

    def __init__(self):
        self.head: Optional[ListNode] = None
        self.size = 0

    def put(self, key: int, value: Any) -> None:
        # TODO: prevent duplicates before allocating a node
        raise NotImplementedError("Student task: linked put")

    def get(self, key: int) -> Any:
        # TODO: advance through current.next until found or exhausted
        raise NotImplementedError("Student task: linked get")

    def delete(self, key: int) -> None:
        # TODO: handle missing, head and non-head deletion
        raise NotImplementedError("Student task: linked delete")

    def contains(self, key: int) -> bool:
        raise NotImplementedError("Student task: linked contains")

    def __len__(self) -> int:
        return self.size


@dataclass
class BSTNode:
    key: int
    value: Any
    left: Optional['BSTNode'] = None
    right: Optional['BSTNode'] = None


class BSTSymbolTable:
    """Plain, unbalanced BST: all left keys < node.key < all right keys."""

    def __init__(self):
        self.root: Optional[BSTNode] = None
        self.size = 0

    def put(self, key: int, value: Any) -> None:
        # TODO: find insertion link or update existing node; protect ordering
        raise NotImplementedError("Student task: BST put")

    def get(self, key: int) -> Any:
        # TODO: descend a single path using the strict invariant
        raise NotImplementedError("Student task: BST get")

    def delete(self, key: int) -> None:
        # TODO: handle leaf, one child and two children; move key AND value
        raise NotImplementedError("Student task: BST delete")

    def contains(self, key: int) -> bool:
        raise NotImplementedError("Student task: BST contains")

    def __len__(self) -> int:
        return self.size
