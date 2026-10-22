"""S01 runnable examples: first-index search, duplicate detection and timings.

Run `python lab.py --self-check` or `python lab.py --benchmark`.
The examples are demonstrations, not answers to exercises.md.
"""

from __future__ import annotations

import argparse
import platform
import statistics
import time
from typing import Sequence


def linear_search(values: Sequence[int], target: int) -> int:
    """Return the first index containing target, or -1 if absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def has_duplicate(values: Sequence[int]) -> bool:
    """Check every unordered pair until a duplicate is found."""
    for first in range(len(values)):
        for second in range(first + 1, len(values)):
            if values[first] == values[second]:
                return True
    return False


def search_comparisons(values: Sequence[int], target: int) -> tuple[int, int]:
    """Return (first matching index or -1, equality-check count)."""
    checks = 0
    for index, value in enumerate(values):
        checks += 1
        if value == target:
            return index, checks
    return -1, checks


def duplicate_comparisons(values: Sequence[int]) -> tuple[bool, int]:
    """Return (has duplicate, equality-check count) in pairwise loop order."""
    checks = 0
    for first in range(len(values)):
        for second in range(first + 1, len(values)):
            checks += 1
            if values[first] == values[second]:
                return True, checks
    return False, checks


def self_check() -> None:
    cases = [
        ([], 4, -1, 0),
        ([4], 4, 0, 1),
        ([4], 9, -1, 1),
        ([9, 4, 4, 1], 4, 1, 2),
        ([9, 4, 4, 1], 7, -1, 4),
    ]
    for values, target, expected_index, expected_checks in cases:
        assert linear_search(values, target) == expected_index
        assert search_comparisons(values, target) == (expected_index, expected_checks)
    duplicate_cases = [
        ([], False, 0),
        ([4], False, 0),
        ([4, 4], True, 1),
        ([3, 8, 5], False, 3),
        ([3, 8, 5, 8], True, 5),
    ]
    for values, expected_result, expected_checks in duplicate_cases:
        assert has_duplicate(values) is expected_result
        assert duplicate_comparisons(values) == (expected_result, expected_checks)
    print("Python self-checks passed (search and duplicate edge cases).")


def median_ns(call, repeats: int = 11) -> int:
    # Warm-up and repeated observations reduce some noise; they do not prove growth.
    call()
    observations = []
    for _ in range(repeats):
        start = time.perf_counter_ns()
        result = call()
        observations.append(time.perf_counter_ns() - start)
        assert result is not None
    return int(statistics.median(observations))


def benchmark() -> None:
    print(f"Python {platform.python_version()} on {platform.platform()}")
    print("Timer: perf_counter_ns; 1 warm-up; median of 11 calls; deterministic inputs")
    print("n, absent_search_comparisons, search_median_ns, distinct_pair_comparisons, pair_median_ns")
    for size in (16, 64, 256, 512):
        values = list(range(size))
        search_checks = search_comparisons(values, -1)[1]
        pair_checks = duplicate_comparisons(values)[1]
        search_time = median_ns(lambda: linear_search(values, -1))
        pair_time = median_ns(lambda: has_duplicate(values))
        print(f"{size}, {search_checks}, {search_time}, {pair_checks}, {pair_time}")
    print("Interpret within this runtime only. Scheduling and timer noise affect small runs.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--benchmark", action="store_true")
    args = parser.parse_args()
    if not args.self_check and not args.benchmark:
        parser.print_help()
    if args.self_check:
        self_check()
    if args.benchmark:
        benchmark()
