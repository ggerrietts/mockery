""" Some sample tests.
"""

import unittest
import summaries
import testcase
from mock import patch, Mock


class MeanTest(unittest.TestCase):

    @patch('summaries.SeriesManager')
    def test_01_empty_series(self, sm):
        self.get_series = gs = sm.get_series
        gs.return_value = []
        retval = summaries.mean_for_series('foofah')
        self.assertEqual(retval, 0)

    def test_02_real_series(self):
        retval = summaries.mean_for_series('plex')
        self.assertEqual(retval, 1.0)


class RefactoredMeanTest(unittest.TestCase):
    """ Refactor to extract some common patching logic
    """

    def _perform_patch(self, series):
        self.get_series = m = Mock(return_value=series)
        sm = Mock(get_series=m)
        return patch.object(summaries, 'SeriesManager', sm)

    def test_01_empty_series(self):
        patcher = self._perform_patch([])
        patcher.start()
        retval = summaries.mean_for_series('foofah')
        patcher.stop()
        self.assertEqual(retval, 0)

    def test_02_real_series(self):
        retval = summaries.mean_for_series('plex')
        self.assertEqual(retval, 1.0)

    def test_03_half_series(self):
        patcher = self._perform_patch([(10, 1, 2), (20, 2, 4), (30, 3, 6)])
        patcher.start()
        retval = summaries.mean_for_series('brobie')
        patcher.stop()
        self.assertEqual(retval, 0.5)


class AlsoBrokenMeanTest(testcase.PatchingTestCase):
    """ Correct the patching!
    """

if __name__ == "__main__":
    unittest.main()
