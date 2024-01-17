"""
home_work_3
"""
from datetime import datetime, timedelta
def find_sundays(year):
    sundays = []
    current_date = datetime(year, 1, 1)
    while current_date.year == year:
        if current_date.weekday() == 6:  # 6 соответствует воскресенью
            sundays.append(current_date)
        current_date += timedelta(days=1)
    return sundays
if __name__ == "__main__":
    year = 2023
    result = find_sundays(year)
    for sunday in result:
        print(sunday.strftime("%A, %d %B %Y"))