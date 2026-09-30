import unittest
from scripts.search_sparse_n5 import mask_from_vertices,canonical_sparse_vertices,search_layer
from scripts.search_n5 import canonical_symmetry

class SparseN5Tests(unittest.TestCase):
    def test_mask_from_vertices(self):
        self.assertEqual(mask_from_vertices((0,2,5)),(1<<0)|(1<<2)|(1<<5))

    def test_small_layer_is_deterministic(self):
        a=search_layer(n=3,k=2); b=search_layer(n=3,k=2)
        self.assertEqual(a["raw"],28)
        self.assertEqual(a["unique_canonical"],b["unique_canonical"])
        self.assertEqual(a["strong_separations"],b["strong_separations"])

if __name__=="__main__": unittest.main()
