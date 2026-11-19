"""Contract tests; DictBaseline is used until student code is complete.

To test your work: change `FACTORY` to ArraySymbolTable, LinkedSymbolTable,
or BSTSymbolTable from `starter`, after implementing its TODO methods.
These are illustrative public tests, not a secret marking suite.
"""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from benchmark import DictBaseline, prepare_keys
# from starter import ArraySymbolTable, LinkedSymbolTable, BSTSymbolTable
FACTORY = DictBaseline


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.t = FACTORY()

    def test_empty_lookup_and_delete(self):
        self.assertEqual(len(self.t), 0)
        self.assertFalse(self.t.contains(1))
        with self.assertRaises(KeyError): self.t.get(1)
        with self.assertRaises(KeyError): self.t.delete(1)

    def test_insert_update_and_none_value(self):
        self.t.put(20, "old")
        self.t.put(30, "other")
        self.t.put(20, None)
        self.assertEqual(len(self.t), 2)
        self.assertTrue(self.t.contains(20))
        self.assertIsNone(self.t.get(20))
        self.assertEqual(self.t.get(30), "other")

    def test_delete_keeps_remaining_values(self):
        for k in [50, 30, 70, 20, 40, 60, 80]:
            self.t.put(k, str(k))
        self.t.delete(50)  # two-child deletion challenge for BST
        self.assertEqual(len(self.t), 6)
        for k in [30, 70, 20, 40, 60, 80]:
            self.assertEqual(self.t.get(k), str(k))
        with self.assertRaises(KeyError): self.t.get(50)

    def test_sorted_and_shuffled_insertions(self):
        for dist in ("sorted", "shuffled"):
            t = FACTORY()
            keys = prepare_keys(20, seed=42, distribution=dist)
            for k in keys: t.put(k, k * 2)
            self.assertEqual(len(t), 20)
            for k in range(20): self.assertEqual(t.get(k), k * 2)


if __name__ == "__main__":
    unittest.main()
