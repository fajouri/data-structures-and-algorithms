#!/usr/bin/env python3
"""S04 teaching demonstrations: stack, FIFO queue, BST-backed key/value table.

Only Python standard library is used. Run --self-check for observable tests.
"""
from __future__ import annotations
import argparse
from collections import deque
from dataclasses import dataclass
from typing import Optional


PAIRS = {")": "(", "]": "[", "}": "{"}


def balanced_delimiters(text: str) -> bool:
    """Check (), [], {} nesting; ignore all other characters."""
    stack: list[str] = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in PAIRS:
            if not stack or stack.pop() != PAIRS[char]:
                return False
    return not stack


def dispatch(tasks: list[str]) -> list[str]:
    """Demonstrate FIFO order without list.pop(0)."""
    pending = deque()
    for task in tasks:
        pending.append(task)
    result: list[str] = []
    while pending:
        result.append(pending.popleft())
    return result


@dataclass
class Node:
    key: int
    value: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BSTMap:
    """Plain unbalanced BST with unique integer keys; missing keys raise KeyError."""
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def put(self, key: int, value: str) -> None:
        def insert(node: Optional[Node]) -> Node:
            if node is None:
                return Node(key, value)
            if key < node.key:
                node.left = insert(node.left)
            elif key > node.key:
                node.right = insert(node.right)
            else:
                node.value = value
            return node
        self.root = insert(self.root)

    def get(self, key: int) -> str:
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        raise KeyError(key)

    def contains(self, key: int) -> bool:
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def delete(self, key: int) -> None:
        def remove(node: Optional[Node], target: int) -> Optional[Node]:
            if node is None:
                raise KeyError(target)
            if target < node.key:
                node.left = remove(node.left, target)
            elif target > node.key:
                node.right = remove(node.right, target)
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.key, node.value = successor.key, successor.value
                node.right = remove(node.right, successor.key)
            return node
        self.root = remove(self.root, key)

    def inorder(self) -> list[int]:
        result: list[int] = []
        def visit(node: Optional[Node]) -> None:
            if node is None:
                return
            visit(node.left)
            result.append(node.key)
            visit(node.right)
        visit(self.root)
        return result


def self_check() -> None:
    assert balanced_delimiters("{a[(b+c)]}")
    assert not balanced_delimiters("([)]")
    assert not balanced_delimiters("(((")
    assert balanced_delimiters("")
    assert dispatch(["T1", "T2", "T3"]) == ["T1", "T2", "T3"]
    tree = BSTMap()
    assert tree.inorder() == []
    for key in (50, 30, 70, 20, 40, 60, 80):
        tree.put(key, f"v{key}")
    assert tree.inorder() == [20, 30, 40, 50, 60, 70, 80]
    assert tree.get(60) == "v60" and not tree.contains(65)
    tree.put(30, "updated")
    assert tree.get(30) == "updated" and len(tree.inorder()) == 7
    tree.delete(20)  # leaf
    tree.delete(30)  # one child: 40
    assert tree.inorder() == [40, 50, 60, 70, 80]
    tree.delete(50)  # two children, successor = 60
    assert tree.inorder() == [40, 60, 70, 80]
    assert tree.root is not None and tree.root.key == 60
    assert tree.get(60) == "v60"
    try:
        tree.get(999)
    except KeyError:
        pass
    else:
        raise AssertionError("Missing get must raise KeyError")
    try:
        tree.delete(999)
    except KeyError:
        pass
    else:
        raise AssertionError("Missing delete must raise KeyError")
    singleton = BSTMap()
    singleton.put(1, "one")
    singleton.delete(1)
    assert singleton.inorder() == []
    print("S04 self-checks passed")


def demo() -> None:
    print("Balanced brackets?", balanced_delimiters("{a[(b+c)]}"))
    print("Crossed brackets?", balanced_delimiters("([)]"))
    print("FIFO order:", dispatch(["ticket A", "ticket B", "ticket C"]))
    tree = BSTMap()
    for key in (50, 30, 70, 20, 40, 60, 80):
        tree.put(key, f"value-{key}")
    print("BST in order:", tree.inorder())
    print("Lookup 60:", tree.get(60))
    tree.delete(50)
    print("After deleting root 50:", tree.inorder())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if args.self_check or not args.demo:
        self_check()
    if args.demo:
        demo()
