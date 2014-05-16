""" Some sample tests.
"""

import unittest
import summaries
from mock import patch, Mock


class SettingUpAMeanTest(unittest.TestCase):
    """ Using setUp and tearDown to set up mocks
    """
    def setUp(self):
        self.get_series = m = Mock()
        sm = Mock(get_series=m)
        self.smpatch = patch.object(summaries, 'SeriesManager', sm)
        self.smpatch.start()

    def tearDown(self):
        self.smpatch.stop()

    def test_01_empty_series(self):
        self.get_series.return_value = []
        retval = summaries.mean_for_series('foofah')
        self.assertEqual(retval, 0)
        self.get_series.assert_called_once()

    def test_03_half_series(self):
        self.get_series.return_value = [(10, 1, 2), (20, 2, 4), (30, 3, 6)]
        retval = summaries.mean_for_series('brobie')
        self.assertEqual(retval, 0.5)
        self.get_series.assert_called_once()


class StandaloneIntegrationTest(unittest.TestCase):
    def test_02_real_series(self):
        retval = summaries.mean_for_series('plex')
        self.assertEqual(retval, 1.0)


if __name__ == "__main__":
    unittest.main()
