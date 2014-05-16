""" Some sample tests.

These are very simple tests.
"""

import unittest
import summaries
from mock import patch


class MeanTest(unittest.TestCase):
    """ Some simple tests to illustrate patching.
    """
    @patch('summaries.SeriesManager')
    def test_01_empty_series(self, sm):
        self.get_series = gs = sm.get_series
        gs.return_value = []
        retval = summaries.mean_for_series('foofah')
        self.assertEqual(retval, 0)
        self.get_series.assert_called_once()

    def test_02_real_series(self):
        retval = summaries.mean_for_series('plex')
        self.assertEqual(retval, 1.0)

    @patch('summaries.SeriesManager')
    def test_03_half_series(self, sm):
        self.get_series = gs = sm.get_series
        gs.return_value = [(10, 1, 2), (20, 2, 4), (30, 3, 6)]
        retval = summaries.mean_for_series('brobie')
        self.assertEqual(retval, 0.5)
        self.get_series.assert_called_once()


if __name__ == "__main__":
    unittest.main()
