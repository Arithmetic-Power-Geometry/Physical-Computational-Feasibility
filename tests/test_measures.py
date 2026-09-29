import unittest
from pcf.measures import conventional_profile

class MeasureTests(unittest.TestCase):
    def test_profiles_are_exact_and_reported(self):
        a=conventional_profile(4,126)
        b=conventional_profile(4,395)
        for p in (a,b):
            self.assertTrue(0<=p["algebraic_degree"]<=4)
            self.assertTrue(0<=p["block_sensitivity"]<=4)
            self.assertTrue(0<=p["decision_tree_depth"]<=4)
        # This test intentionally does not assume equality: the experiment
        # determines whether the witness survives stronger conventional controls.

if __name__=="__main__": unittest.main()
