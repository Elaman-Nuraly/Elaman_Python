"""
home_work_5
"""
from datetime import datetime, timezone, timedelta
def get_gmt_local_time():
    gmt_time = datetime.now(timezone.utc)
    local_time = datetime.now()
    return gmt_time, local_time
if __name__ == "__main__":
    gmt_time, local_time = get_gmt_local_time()
    print(f"Время по Гринвичу: {gmt_time}")
    print(f"Местное время: {local_time}")