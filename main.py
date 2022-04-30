import os
import vestaboard
#This will print your subscription ID, and store all keys in 'credentials.txt'
installable = vestaboard.Installable(os.environ['api_key'], os.environ['api_secret'])
#Pass in the Installable() instance to a new instance of Board()
vboard = vestaboard.Board(installable)
#vboard.post(str())
import python_weather
import asyncio

# Python program to find current
# weather details of any city
# using openweathermap api
 
# import required modules
import requests, json
 
# Enter your API key here
api_key = "cf904326a86efdee62264d5205252acf"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
#city_name = input("Enter city name : ")
 
# complete_url variable to store
# complete url address
#complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
lat = "40.78255943661178"
lon = "-73.95564993117083"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)

from flask import Flask
app = Flask('app')
@app.route('/')
def main():
    return 'Hello!'
@app.route('/weather')
def weather():
    response = requests.get(url)
    data = json.loads(response.text)
    #vboard.post(data)
    current = data["current"]["temp"]
    feels_like = data["current"]["feels_like"]
    wind_speed = data["current"]["wind_speed"]
    description = data["current"]["weather"][0]["description"]
    intro = "{63}{64}Current NY Weather{63}{64}\n"
    ending = "{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}"
    vboard.post(intro + "Temperature: " + str(current) + "°\n" + "Feels Like: " + str(feels_like) + "\nWind Speed: " + str(wind_speed) + "\nDescription: " + str(description) + "\n" + ending)
    return 'Success!'
@app.route('/morningRemind')
def reminders():
    intro = "School Checklist Time!"
    ending = "{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}"
    vboard.post(intro + """
Be sure to Pack:
Library Book(s)
Homework
Get your mask, jacket, shoes and backpack on!""")
    return 'Success!'
@app.route('/theWeekend')
def weekend():
    intro = "Non-School Checklist Time!"
    ending = "{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}"
    vboard.post(intro + """
IT'S THE WEEKEND! YAYYYY""")
    return 'Success!'
@app.route('/dadJoke')
def dadJoke():
    url = "https://daddyjokes.p.rapidapi.com/random"

    headers = {
	"X-RapidAPI-Host": "daddyjokes.p.rapidapi.com",
	"X-RapidAPI-Key": "280c0ff849msh21ae5907561ac4bp1d00b8jsn691392cf51fb"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    
    intro = "Who's ready for a joke?\n"
    ending = "{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}{67}{68}"
    #print(data)
    vboard.post(data["joke"])
    return 'Success!'
app.run(host='0.0.0.0', port=80)
