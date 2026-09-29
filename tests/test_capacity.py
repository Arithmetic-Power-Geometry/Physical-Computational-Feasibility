import unittest
from pcf.capacity import shared_endpoint_capacity,component_serial_rounds

class CapacityTests(unittest.TestCase):
    def test_endpoint_conflict_does_not_separate_spectral_pair(self):
        a=shared_endpoint_capacity(4,126,100)
        b=shared_endpoint_capacity(4,395,100)
        # Both have maximum sensitivity 3, so bipartite edge coloring needs 3 rounds.
        self.assertEqual(a.exact_edge_coloring_rounds,3)
        self.assertEqual(b.exact_edge_coloring_rounds,3)

    def test_matching_diff_is_real_but_not_round_complexity_here(self):
        a=shared_endpoint_capacity(4,126,100)
        b=shared_endpoint_capacity(4,395,100)
        self.assertEqual(a.matching_number,6)
        self.assertEqual(b.matching_number,5)

    def test_component_serial_model(self):
        a=component_serial_rounds(4,126)
        b=component_serial_rounds(4,395)
        self.assertEqual(len(a[1]),2)
        self.assertEqual(len(b[1]),2)

if __name__=="__main__": unittest.main()
