import unittest
from pcf.measures import xor_with_parity, conventional_profile,real_polynomial_degree

class MeasureTests(unittest.TestCase):
    def test_real_polynomial_degree(self):
        # XOR on two bits: x+y-2xy has real degree 2.
        self.assertEqual(real_polynomial_degree(2,0b0110),2)

    def test_correct_f126_profile(self):
        self.assertEqual(conventional_profile(4,126),{
            "block_sensitivity":3,
            "algebraic_degree":3,
            "real_polynomial_degree":3,
            "certificate_complexity":(3,3,3),
            "decision_tree_depth":4,
        })

    def test_correct_f395_profile(self):
        self.assertEqual(conventional_profile(4,395),{
            "block_sensitivity":3,
            "algebraic_degree":4,
            "real_polynomial_degree":4,
            "certificate_complexity":(3,2,3),
            "decision_tree_depth":4,
        })

if __name__=="__main__": unittest.main()


class ParityLiftTests(unittest.TestCase):
    def test_k5_pair_parity_lift_r1_preserves_matched_profile(self):
        from pcf.measures import conventional_profile
        a,b=1878982398,65833
        A=xor_with_parity(5,a,1); B=xor_with_parity(5,b,1)
        self.assertEqual(conventional_profile(6,A),conventional_profile(6,B))
