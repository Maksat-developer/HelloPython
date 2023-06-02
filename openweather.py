import requests
import datetime

open_weather_token = '34cf6a25808cceed9d3c705259d2c952'
city = input("City: ")

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru")
data = r.json()


if 'name' in data:
    city = data["name"]
    des = data["weather"][0]["description"]
    cur_weath = data["main"]["temp"]
    press = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    country = data["sys"]["country"]
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

    print(f"⚡️☄️💥🔥🌪 {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')} 🌪🔥💥☄️⚡️\n️"
          f"Название города: {city}\n"
          f"Текущая погода: {des}\n"
          f"Температура воздуха: {cur_weath}°C\n"
          f"Атмосферное давление: {press} мм.рт.ст.\n"
          f"Влажность воздуха: {humidity}%\n"
          f"Скорость ветра: {wind} м/с\n"
          f"Код страны: {country}\n"
          f"Восход: {sunrise}")
else:
    print("Не удалось получить данные о погоде. Проверьте название города!")
