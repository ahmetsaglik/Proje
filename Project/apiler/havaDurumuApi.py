def tranlate(text):
    skyTypes = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']
    skyTypesTR = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']

    for i in range(len(skyTypes)):
        if text == skyTypes[i]:
            text = skyTypesTR[i]
    return text

def havaDurumu(city):
    import requests
    import json

    apiKey = "c30fcd9f7f797bca44ff8ef427fd36e1"
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}")

    weatherData = response.json()
    skyDesp = weatherData["weather"][0]["description"]
    skyDesp = tranlate(skyDesp)

    temperature = round((weatherData["main"]["temp"] - 273.15),2)
    feelsTemperature = round((weatherData["main"]["feels_like"] - 273.15),2)
    minTemperature = round((weatherData["main"]["temp_min"] - 273.15),2)
    maxTemperature = round((weatherData["main"]["temp_max"] - 273.15),2)
    
    resp = f" Şehir: {city} \n Hava Durumu: {skyDesp} \n Sıcaklık: {temperature} \n Hissedilen Sıcaklık: {feelsTemperature} \n Minimum Sıcaklık: {minTemperature} \n Maximum Sıcaklık: {maxTemperature}"
    return resp
