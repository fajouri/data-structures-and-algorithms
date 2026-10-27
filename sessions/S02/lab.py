#!/usr/bin/env python3
"""S02 lab: recursive traces, recurrence examples and binary-search testing.

Python 3; standard library only. This is student-facing starter material, not an answer key.
"""
from __future__ import annotations

import argparse
from typing import Sequence


def factorial(n: int) -> int:
    """Return n! for n >= 0; reject inputs outside the contract."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def binary_search(values: Sequence[int], target: int) -> int:
    """Return any matching index or -1. values must be sorted ascending."""
    lo, hi = 0, len(values)  # half-open interval [lo, hi)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return -1


def binary_search_recursive(
    values: Sequence[int], target: int, lo: int = 0, hi: int | None = None
) -> int:
    """Recursive binary search using a half-open interval [lo, hi)."""
    if hi is None:
        hi = len(values)
    if lo >= hi:
        return -1
    mid = lo + (hi - lo) // 2
    if values[mid] == target:
        return mid
    if values[mid] < target:
        return binary_search_recursive(values, target, mid + 1, hi)
    return binary_search_recursive(values, target, lo, mid)


def self_check() -> None:
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("factorial must reject negative input")

    cases = [
        ([], 4, -1),
        ([7], 7, 0),
        ([7], 2, -1),
        ([1, 3, 4, 6, 8, 10, 14, 17], 10, 5),
        ([1, 3, 4, 6, 8, 10, 14, 17], 1, 0),
        ([1, 3, 4, 6, 8, 10, 14, 17], 17, 7),
        ([1, 3, 4, 6, 8, 10, 14, 17], 2, -1),
        ([1, 3, 4, 6, 8, 10, 14, 17], 7, -1),
        ([1, 3, 4, 6, 8, 10, 14, 17], 20, -1),
    ]
    for values, target, expected in cases:
        actual = binary_search(values, target)
        assert actual == expected, (values, target, actual, expected)
        recursive = binary_search_recursive(values, target)
        assert recursive == expected, (values, target, recursive, expected)

    # With duplicates, either implementation may return any matching index.
    values = [2, 2, 2, 5, 5, 9]
    for search in (binary_search, binary_search_recursive):
        idx = search(values, 5)
        assert idx != -1 and values[idx] == 5

    print("Self-check passed.")


def demo() -> None:
    print("factorial(5):", factorial(5))
    values = [2, 4, 7, 9, 13, 18, 21]
    for target in (13, 8, 2, 21):
        idx = binary_search(values, target)
        print(f"target={target:2d} -> index={idx}")
    print("Analyse by hand: T(n)=T(n-1)+Theta(1)")
    print("Analyse by hand: T(n)=2T(n/2)+Theta(n)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-check", action="store_true")
    group.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
    else:
        demo()


if __name__ == "__main__":
    main()
