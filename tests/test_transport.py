import unittest
from pcf.transport import optimize_line,optimize_refresh_line

class TransportTests(unittest.TestCase):
    def test_matched_pair_same_simple_line_transport(self):
        # This model depends only on which input bit flips each sensitive edge.
        # A difference is not assumed; equality is a scientifically useful falsification.
        a=optimize_line(4,126,0.9,0.1)
        b=optimize_line(4,395,0.9,0.1)
        self.assertEqual(a.failed_edges,b.failed_edges)

    def test_refresh_optimizer_runs(self):
        for mask in (126,395):
            z,total,worst=optimize_refresh_line(4,mask,0.9,0.1)
            self.assertGreaterEqual(total,0); self.assertGreaterEqual(worst,0)

if __name__=="__main__": unittest.main()
