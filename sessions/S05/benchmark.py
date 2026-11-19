#!/usr/bin/env python3
"""S05 reproducible benchmark teaching harness.

Default table is a built-in dict baseline, NOT an Assignment 1 implementation.
Student implementations are intentionally NOT registered until correct.
Run: python benchmark.py --sizes 100 500 1000 --repeats 5
"""
import argparse
import platform
import random
import statistics
import sys
import time
from pathlib import Path


class DictBaseline:
    """Working behavioural reference. Internal storage: Python dict."""
    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]

    def delete(self, key):
        del self.data[key]

    def contains(self, key):
        return key in self.data

    def __len__(self):
        return len(self.data)


def prepare_keys(n, seed=42, distribution="shuffled"):
    keys = list(range(n))
    if distribution == "shuffled":
        random.Random(seed).shuffle(keys)
    elif distribution != "sorted":
        raise ValueError("Unknown distribution")
    return keys


def contract_smoke_test(factory):
    """Selected test examples, not a formal proof."""
    t = factory()
    assert len(t) == 0
    try:
        t.get(123)
        raise AssertionError("missing get must raise KeyError")
    except KeyError:
        pass
    t.put(20, "a")
    t.put(40, "b")
    t.put(20, None)
    assert len(t) == 2 and t.contains(20) and t.get(20) is None
    t.delete(40)
    assert len(t) == 1 and not t.contains(40)
    try:
        t.delete(40)
        raise AssertionError("missing delete must raise KeyError")
    except KeyError:
        pass
    return True


def time_gets(table, lookup_keys):
    """Only get operations are timed; table setup is excluded."""
    start = time.perf_counter_ns()
    checksum = 0
    for key in lookup_keys:
        checksum += table.get(key)
    elapsed = time.perf_counter_ns() - start
    return elapsed, checksum


def median_lookup_us(factory, keys, repeats=5):
    """Report microseconds per successful lookup; repeat complete lookup batches."""
    table = factory()
    for k in keys:
        table.put(k, k)
    query_keys = list(keys)  # identical hit queries for each implementation
    expected_checksum = sum(query_keys)
    time_gets(table, query_keys)  # warm-up, not recorded
    timings = []
    for _ in range(repeats):
        duration, checksum = time_gets(table, query_keys)
        assert checksum == expected_checksum
        timings.append(duration / len(query_keys) / 1000.0)
    return statistics.median(timings)


def factories():
    available = {"Python-dict-baseline": DictBaseline}
    # AFTER correctness tests pass, optionally register student classes:
    # from starter import ArraySymbolTable, LinkedSymbolTable, BSTSymbolTable
    # available.update({"array": ArraySymbolTable,
    #                   "linked": LinkedSymbolTable,
    #                   "BST": BSTSymbolTable})
    return available


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", nargs="+", type=int, default=[100, 500, 1000])
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--distribution", choices=["sorted", "shuffled"], default="shuffled")
    args = parser.parse_args()
    if any(n <= 0 for n in args.sizes) or args.repeats < 2:
        parser.error("sizes must be positive and repeats >= 2")
    print("Python:", sys.version.split()[0], "| OS:", platform.platform())
    print("Seed:", args.seed, "| Distribution:", args.distribution, "| Repeats:", args.repeats)
    print("table,n,workload,median_us_per_operation,repeats,correctness_passed")
    for name, factory in factories().items():
        contract_smoke_test(factory)
        for n in args.sizes:
            keys = prepare_keys(n, args.seed, args.distribution)
            metric = median_lookup_us(factory, keys, args.repeats)
            print(f"{name},{n},hit-get,{metric:.6f},{args.repeats},yes")
    print("NOTE: dict baseline is not an assignment implementation. No comparison claim is implied.")


if __name__ == "__main__":
    main()
