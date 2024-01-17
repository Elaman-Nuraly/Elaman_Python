"""
home_work_1
"""
from datetime import datetime

def get_week_number(year, month, day):
    date_object = datetime(year, month, day)
    week_number = date_object.isocalendar()[1]
    return week_number
if __name__ == "__main__":
    year = 2015
month = 6
day = 16
result = get_week_number(year, month, day)
print("Output:", result)