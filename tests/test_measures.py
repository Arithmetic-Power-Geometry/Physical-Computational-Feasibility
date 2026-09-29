import unittest
from pcf.measures import conventional_profile

class MeasureTests(unittest.TestCase):
    def test_correct_f126_profile(self):
        self.assertEqual(conventional_profile(4,126),{
            "block_sensitivity":3,
            "algebraic_degree":3,
            "certificate_complexity":(3,3,3),
            "decision_tree_depth":4,
        })

    def test_correct_f395_profile(self):
        self.assertEqual(conventional_profile(4,395),{
            "block_sensitivity":3,
            "algebraic_degree":4,
            "certificate_complexity":(3,3,2),
            "decision_tree_depth":4,
        })

if __name__=="__main__": unittest.main()
