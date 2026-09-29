import unittest
from scripts.search_n5 import canonical_complement,search

class N5SearchTests(unittest.TestCase):
    def test_complement_canonicalization(self):
        n=5; full=(1<<(1<<n))-1; m=1234567
        self.assertEqual(canonical_complement(n,m),canonical_complement(n,full^m))

    def test_deterministic_small_search(self):
        a=search(samples=100,seed=7); b=search(samples=100,seed=7)
        self.assertEqual(a["unique"],b["unique"])
        self.assertEqual(a["cheap_collisions"],b["cheap_collisions"])

if __name__=="__main__": unittest.main()
