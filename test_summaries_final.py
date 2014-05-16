""" Some sample tests.

These have been refactored to use the PatchingTestCase
"""

import unittest
import summaries
import testcase
from mock import Mock

class RefactoredMeanTest(testcase.PatchingTestCase):
    """ A more thorough refactoring
    """

    def _patch_series_manager(self, series):
        self.get_series = m = Mock(return_value=series)
        sm = Mock(get_series=m)
        return self.patch(summaries, 'SeriesManager', sm)

    def test_01_empty_series(self):
        self._patch_series_manager([])
        retval = summaries.mean_for_series('foofah')
        self.assertEqual(retval, 0)
        self.get_series.assert_called_once()

    def test_02_real_series(self):
        retval = summaries.mean_for_series('plex')
        self.assertEqual(retval, 1.0)

    def test_03_half_series(self):
        self._patch_series_manager([(10, 1, 2), (20, 2, 4), (30, 3, 6)])
        retval = summaries.mean_for_series('brobie')
        self.assertEqual(retval, 0.5)
        self.get_series.assert_called_once()



if __name__ == "__main__":
    unittest.main()
