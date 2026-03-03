from datetime import datetime 
from pandas import NaT

import constants


def parse_dates(date_val: str):
        for format in constants.DATE_FORMATS:
            try:
                return datetime.strptime(date_val, format)
            except ValueError: 
                continue
        # No match found
        return NaT
