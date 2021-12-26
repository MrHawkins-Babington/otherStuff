#ISS finder
#Find out the current Latitude and Longitude of the International Space Station
#Find out who is currently on board the ISS
#Find out when the ISS is next in the sky above your location

#import python modules
import json
import urllib.request
import turtle
import time
import webbrowser
import os

#This bit added because of issues using the code in the school system
url = 'http://api.open-notify.org/astros.json'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open_new(url)
time.sleep(2)
os.system("taskkill /IM chrome.exe /f")


#Who is in space?
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
	print(p['name'], ' in ', p['craft'])


#Where are they right now?
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)


#Make a window
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.register_shape('iss.gif')
screen.bgpic('map.gif')


#place the iss on the map in the window
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(lon, lat)


# When Does ISS next pass over me?
#put a yellow dot on Gütersloh, Germany
lat = 51.9063
lon = 8.3782

###Oregon
##lat = 45
##lon = 122.3

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()


#put a time and date by the yellow dot (time is UTC not local time)
url = 'http://api.open-notify.org/iss-pass.json?lat='+ str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][0]['risetime'] #change number 0 to 5 and see what happens
location.write(time.ctime(over))


#when I started creating this file the ISS was over South America.
#As I type this it is over North West Africa
