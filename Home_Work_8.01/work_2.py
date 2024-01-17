"""
home_work_2
"""
from datetime import datetime, timedelta
def find_first_monday(year, week):
    first_day = datetime(year, 1, 1)
    first_week_day = first_day - timedelta(days=first_day.weekday())
    target_date = first_week_day + timedelta(weeks=week-1)
    while target_date.weekday() != 0:
        target_date += timedelta(days=1)
    return target_date
if __name__ == "__main__":
    year = 2015
    week = 50
    result = find_first_monday(year, week)
    print("Output:", result)
    