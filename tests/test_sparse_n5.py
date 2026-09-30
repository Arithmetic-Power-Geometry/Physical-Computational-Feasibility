import unittest
from scripts.search_sparse_n5 import mask_from_vertices,canonical_sparse_vertices,search_layer,verify_witness_pair
from scripts.search_n5 import canonical_symmetry
from pcf.boolean_geometry import characteristic_polynomial_active, truth_set

class SparseN5Tests(unittest.TestCase):
    def test_mask_from_vertices(self):
        self.assertEqual(mask_from_vertices((0,2,5)),(1<<0)|(1<<2)|(1<<5))

    def test_k5_witness_exact_spectrum_and_truth_sets(self):
        a,b=1878982398,65833
        self.assertEqual(len(truth_set(5,a)),5)
        self.assertEqual(len(truth_set(5,b)),5)
        self.assertEqual(characteristic_polynomial_active(5,a),
                         characteristic_polynomial_active(5,b))

    def test_k5_discovered_pair_matches_strong_summary_but_not_geometry(self):
        r=verify_witness_pair(5,1878982398,65833)
        self.assertTrue(r["same_strong_key"])
        self.assertTrue(r["different_residual"])
        self.assertEqual(r["residual_a"],((16,4),5,(6,2)))
        self.assertEqual(r["residual_b"],((11,9),5,(4,4)))

    def test_small_layer_is_deterministic(self):
        a=search_layer(n=3,k=2); b=search_layer(n=3,k=2)
        self.assertEqual(a["raw"],28)
        self.assertEqual(a["unique_canonical"],b["unique_canonical"])
        self.assertEqual(a["strong_separations"],b["strong_separations"])

if __name__=="__main__": unittest.main()
