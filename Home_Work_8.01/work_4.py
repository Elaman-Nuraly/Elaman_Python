"""
home_work_4
"""
from datetime import datetime, timedelta
def add_years(input_date, years_to_add):
    try:
        date_object = datetime.strptime(str(input_date), '%Y-%m-%d')
        new_date = date_object + timedelta(days=365 * years_to_add)
        return new_date.strftime('%Y-%m-%d')
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None
if __name__ == "__main__":
    print(add_years(datetime.date(2015, 1, 1), -1))
    print(add_years(datetime.date(2015, 1, 1), 0))
    print(add_years(datetime.date(2015, 1, 1), 2))
    print(add_years(datetime.date(2000, 2, 29), 1))