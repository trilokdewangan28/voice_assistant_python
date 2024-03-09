import wikipedia
from speak import Spk
# import listen
# import speak
# import random
import requests
from bs4 import BeautifulSoup
import bs4

"""
sentence = "what is guru ghasidas university"
print("something is there....." + sentence)
url = "https://www.google.com/search?q=" + sentence
html = requests.get(url).content
data = bs4.BeautifulSoup(html, 'html.parser')
#print(data.prettify())
result = data.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text
print(result)
"""

# cmd = listen.takeCommand()
# list = ['play song','make my mood','play music']
# list2 = random.choice(list)
# list3= "".join(list2)
# print(list3)


# finding temprature and use in main.py file
try:
    # enter city name
    city = "temprature in bilaspur chhattisgarh"
    # create url
    url = "https://www.google.com/search?q=" + city
    # requests instance
    r = requests.get(url)
    # getting raw data
    data = bs4.BeautifulSoup(r.text, 'html.parser')
    temprature = data.find("div", class_="BNeawe").text
    temprature2 = "current temp:" + temprature

    """
    try:
        wp ="what is java"
        result=wikipedia.summary(wp)
        print(result)
    except Exception as ex:
        print(ex)
    """
except Exception as ex:
    Spk.say("An exception occurred" + ex)
