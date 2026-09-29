import unittest
from pcf.layout import fixed_hypercube_coordinate_wirelength

class LayoutTests(unittest.TestCase):
    def test_natural_hypercube_layout_is_blind(self):
        self.assertEqual(fixed_hypercube_coordinate_wirelength(4,126),12)
        self.assertEqual(fixed_hypercube_coordinate_wirelength(4,395),12)

if __name__=="__main__": unittest.main()
