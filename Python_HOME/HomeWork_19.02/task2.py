import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.gismeteo.kz/weather-astana-5205/")

if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    temp_block = soup.find("div", class_="temp")

    weather_text = temp_block.get_text(strip=True)

    print("Погода в городе Астана:", weather_text)
else:
    print("Не удалось получить данные о прогнозе погоды")
