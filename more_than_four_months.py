from datetime import datetime
from dateutil.relativedelta import relativedelta

date1 = '2024-11-08'
date2 = '2024-07-07'

def more_than_120_days():
    diff = relativedelta(datetime.strptime(date1, '%Y-%m-%d'), datetime.strptime(date2, '%Y-%m-%d'))
    return False if (diff.months < 4 or (diff.months == 4 and diff.days == 0)) else True

print(more_than_120_days())

date2 = '2024-07-08'

print(more_than_120_days())

date2 = '2024-07-09'

print(more_than_120_days())
