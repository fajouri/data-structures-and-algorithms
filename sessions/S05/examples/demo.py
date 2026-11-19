#!/usr/bin/env python3
"""Run from sessions/S05 or from the repo root. No assignment solutions."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from benchmark import DictBaseline, contract_smoke_test, prepare_keys


def main():
    contract_smoke_test(DictBaseline)
    print("Teaching-only dict baseline: contract smoke tests passed.")
    for distribution in ("sorted", "shuffled"):
        keys = prepare_keys(8, seed=42, distribution=distribution)
        print(f"{distribution} keys (n=8, seed=42): {keys}")
    print("Next: write invariant, implement one starter method, run tests, then benchmark.")


if __name__ == "__main__":
    main()
