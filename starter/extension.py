import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

start_session = pd.Timestamp('2016-01-04', tz='utc')
end_session = pd.Timestamp('2099-01-01', tz='utc')

register(
    'hose',
    csvdir_equities(
        ['daily'],
        '/home/user/documents/project/csvdir',
    ),
    calendar_name='HOSE',  # HOSE Vietnam
    start_session=start_session,
    end_session=end_session
)
