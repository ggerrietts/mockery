""" A sample module to write tests against.
"""

import collections

# In a typical application we would do:
# from some_module import SeriesManager

# but since we're fudging things, let's just fudge them:
class SeriesManager(object):
    def get_series(self, series_name):
        return [(10, 1, 1), (20, 2, 2), (30, 3, 3)]


SeriesPoint = collections.namedtuple('SeriesPoint', ['time', 'total', 'count'])


def mean_for_series(series_name):
    """ Calls a pretend service to retrieve a timeseries
    """
    raw_series = SeriesManager.get_series(series_name)
    series = [SeriesPoint(*row) for row in raw_series]
    grand_total = sum(x.total for x in series)
    total_count = sum(x.count for x in series)
    return grand_total / float(total_count)
