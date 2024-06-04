import eel
import pyowm

owm = pyowm.OWM("d5333f2d6478120a6bbb2ca1950eb380")

@eel.expose
def get_weather(place):

    city = place
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)

    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + city + " сейчас " + str(temp) + " °C!"


eel.init("web")
eel.start("main.html", size=(700, 950))

# 5 пжалста :D
# с этим кодом было много проблем ¯\_(ツ)_/¯