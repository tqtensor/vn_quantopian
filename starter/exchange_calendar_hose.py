# # # # # # # # # # # # #
#  cryptocean project   #
# # # # # # # # # # # # #

from datetime import time
import pandas as pd
from pytz import timezone
from .precomputed_trading_calendar import PrecomputedTradingCalendar

from io import BytesIO
import requests

"""
Precomputed holidays are stored on the Google Spreadsheet
"""
r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTH623s5LSTmljwPPqSlYniruc8u3OF16et08zYVsgPEno1cLAkCG0wsfhxsaCjTyl6suKOywDcWTVN/pub?gid=0&single=true&output=csv')
dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
df = pd.read_csv(BytesIO(r.content), parse_dates=['date'], date_parser=dateparse)

precomputed_hose_holidays = pd.to_datetime(df.date)

class HOSEExchangeCalendar(PrecomputedTradingCalendar):
    """
    Exchange calendar for the Ho Chi Minh City Stock Exchange (HOSE).

    The holidays are precomputed and provided via Google Spreadsheet.

    Open Time: 9:00 Asia/Ho_Chi_Minh
    Close Time: 15:00 Asia/Ho_Chi_Minh
    """

    name = 'HOSE'

    tz = timezone('Asia/Ho_Chi_Minh')

    open_times = (
        (None, time(9, 1)),
    )

    close_times = (
        (None, time(15, 0)),
    )

    @property
    def precomputed_holidays(self):
        return precomputed_hose_holidays
