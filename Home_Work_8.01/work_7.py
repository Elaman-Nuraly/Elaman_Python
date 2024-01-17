"""
home_work_7
"""
from datetime import datetime
def diff_to_days_hours_minutes_seconds(diff):
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds
if __name__ == "__main__":
    date_str1 = "2022-01-01 12:00:00"
    date_str2 = "2022-01-05 18:30:45"
    date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
    time_difference = date2 - date1
    days, hours, minutes, seconds = diff_to_days_hours_minutes_seconds(time_difference)
    print(f"Разница между {date_str1} и {date_str2}: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")