import requests

response = requests.get("https://www.gismeteo.kz/weather-astana-5205/")

if response.status_code == 200:
    html_content = response.text

    start_tag = "<div class=\"temp\">"
    end_tag = "</div>"
    start_index = html_content.find(start_tag)
    end_index = html_content.find(end_tag, start_index)

    weather_text = html_content[start_index + len(start_tag):end_index].strip()

    print("Погода в городе Астана:", weather_text)
else:
    print("Не удалось получить данные о прогнозе погоды")
