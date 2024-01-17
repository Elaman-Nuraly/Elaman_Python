"""
home_work_6
"""
from datetime import datetime
def days_between_dates(date1, date2):
    # Преобразуем строки с датами в объекты datetime
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    delta = date2 - date1
    return delta.days
if __name__ == "__main__":
    date_str1 = "2022-01-01"
    date_str2 = "2022-12-31"
    result = days_between_dates(date_str1, date_str2)
    print(f"Количество дней между {date_str1} и {date_str2}: {result} дней")