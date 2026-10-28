#!/usr/bin/env python3
"""S03 lab: dynamic-array accounting and singly linked list; standard library only."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from typing import Optional


def insert_at(values: list[int], index: int, value: int) -> None:
    if not 0 <= index <= len(values):
        raise IndexError("index must be between zero and len(values)")
    values.insert(index, value)


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


class SinglyLinkedList:
    """Teaching implementation with head, tail and size invariants."""
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def append(self, value: int) -> None:
        node = Node(value)
        if self.tail is None:
            assert self.head is None and self.size == 0
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value: int) -> None:
        node = Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def find(self, value: int) -> Optional[Node]:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def insert_after(self, predecessor: Node, value: int) -> None:
        current = self.head
        while current is not None and current is not predecessor:
            current = current.next
        if current is None:
            raise ValueError("predecessor does not belong to this list")
        node = Node(value, predecessor.next)
        predecessor.next = node
        if self.tail is predecessor:
            self.tail = node
        self.size += 1

    def remove_first(self, value: int) -> bool:
        previous: Optional[Node] = None
        current = self.head
        while current is not None and current.value != value:
            previous, current = current, current.next
        if current is None:
            return False
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        if self.tail is current:
            self.tail = previous
        self.size -= 1
        if self.size == 0:
            self.head = self.tail = None
        return True

    def to_list(self) -> list[int]:
        result: list[int] = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def check_invariant(self) -> None:
        values = self.to_list()
        assert len(values) == self.size
        assert (self.size == 0) == (self.head is None)
        assert (self.size == 0) == (self.tail is None)
        if self.tail is not None:
            assert self.tail.next is None and values[-1] == self.tail.value


def dynamic_array_copy_trace(count: int) -> tuple[int, list[tuple[int, int, int]]]:
    """Return total copies and rows (size after append, capacity, copies this append)."""
    if count < 0:
        raise ValueError("count must be non-negative")
    size, capacity, total = 0, 1, 0
    rows: list[tuple[int, int, int]] = []
    for _ in range(count):
        copied = 0
        if size == capacity:
            copied = size
            total += copied
            capacity *= 2
        size += 1
        rows.append((size, capacity, copied))
    return total, rows


def self_check() -> None:
    values = [10, 20, 30, 40]
    insert_at(values, 2, 25)
    assert values == [10, 20, 25, 30, 40]
    try:
        insert_at(values, 99, 1)
    except IndexError:
        pass
    else:
        raise AssertionError("invalid index must raise IndexError")

    linked = SinglyLinkedList()
    linked.check_invariant()
    linked.append(20)
    linked.prepend(10)
    linked.append(30)
    predecessor = linked.find(10)
    assert predecessor is not None
    linked.insert_after(predecessor, 15)
    assert linked.to_list() == [10, 15, 20, 30]
    linked.check_invariant()
    assert linked.remove_first(20)
    assert linked.to_list() == [10, 15, 30]
    assert not linked.remove_first(999)
    for value in (10, 15, 30):
        assert linked.remove_first(value)
        linked.check_invariant()
    assert linked.to_list() == []
    assert dynamic_array_copy_trace(9)[0] == 15
    assert dynamic_array_copy_trace(9)[1][-1] == (9, 16, 8)
    print("Self-check passed.")


def demo() -> None:
    total, trace = dynamic_array_copy_trace(9)
    print("size capacity copies-this-append")
    for row in trace:
        print(*row)
    print("total copied elements:", total)
    linked = SinglyLinkedList()
    for value in (10, 20, 30):
        linked.append(value)
    predecessor = linked.find(10)
    assert predecessor is not None
    linked.insert_after(predecessor, 15)
    print("linked list after insertion:", linked.to_list())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-check", action="store_true")
    group.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    self_check() if args.self_check else demo()


if __name__ == "__main__":
    main()
