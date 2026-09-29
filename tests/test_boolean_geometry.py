import math
import unittest
from pcf.boolean_geometry import analyze, truth_set

class GeometryWitnessTests(unittest.TestCase):
    def test_scalar_profile_matches(self):
        a,b=analyze(4,111),analyze(4,393)
        self.assertEqual(a.scalar_signature,b.scalar_signature)
        self.assertEqual(len(a.essential_variables),4)
        self.assertEqual(len(a.sensitive_edges),12)
        self.assertEqual(a.max_sensitivity,3)
        self.assertEqual(a.degree_histogram,((0,2),(1,8),(2,2),(3,4)))
    def test_geometry_separates(self):
        a,b=analyze(4,111),analyze(4,393)
        self.assertEqual(a.active_component_sizes,(10,2,2))
        self.assertEqual(b.active_component_sizes,(6,4,4))
        self.assertEqual(a.matching_number,6); self.assertEqual(b.matching_number,4)
        self.assertEqual(a.active_diameters,(6,1,1)); self.assertEqual(b.active_diameters,(4,2,2))
        self.assertTrue(math.isclose(a.spectral_radius,math.sqrt(6),rel_tol=1e-8))
        self.assertTrue(math.isclose(b.spectral_radius,math.sqrt(5),rel_tol=1e-8))
    def test_truth_sets(self):
        self.assertEqual(truth_set(4,111),("0000","0001","0010","0011","0101","0110"))
        self.assertEqual(truth_set(4,393),("0000","0011","0111","1000"))
if __name__=="__main__": unittest.main()
