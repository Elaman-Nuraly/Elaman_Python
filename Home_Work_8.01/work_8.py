"""
home_work_8
"""
import calendar
def generate_html_calendar(year, month):
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    calendar_html = cal.formatmonth(year, month)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calendar</title>
    </head>
    <body>
        <h2>{cal.month[month]} {year}</h2>
        {calendar_html}
    </body>
    </html>
    """
    if __name__ == "__main__":
        with open("calendar.html", "w") as file:
            file.write(html)
    generate_html_calendar(2023, 12)