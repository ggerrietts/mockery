""" Some sample tests.

These have been refactored to extract out the configuration logic
"""

import unittest
import summaries
from mock import patch


class RevisedMeanTest(unittest.TestCase):
    """ A first pass at refactoring out common logic
    """
    def _set_up_series_mgr(self, series_mgr, series):
        self.get_series = series_mgr.get_series
        self.get_series.return_value = series

    @patch('summaries.SeriesManager')
    def test_01_empty_series(self, sm):
        self._set_up_series_mgr(sm, [])
        retval = summaries.mean_for_series('foofah')
        self.assertEqual(retval, 0)
        self.get_series.assert_called_once()

    def test_02_real_series(self):
        retval = summaries.mean_for_series('plex')
        self.assertEqual(retval, 1.0)

    @patch('summaries.SeriesManager')
    def test_03_half_series(self, sm):
        self._set_up_series_mgr(sm, [(10, 1, 2), (20, 2, 4), (30, 3, 6)])
        retval = summaries.mean_for_series('brobie')
        self.assertEqual(retval, 0.5)
        self.get_series.assert_called_once()


if __name__ == "__main__":
    unittest.main()
