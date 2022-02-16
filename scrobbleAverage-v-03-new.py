# I use last.fm to scrobble all of the music I listen to.
# Each month I have an average listen count
# I wanted to be able to work out how many tracks a day I needed to listen to,
# To allow me to achieve a particular play count average.


import math
import calendar
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
d2 = today.strftime("%d")
d3 = today.strftime("%m")
d4 = today.strftime("%Y")

print("Today's date =", d1)
print("The current day =", d2)
print("the current month =", d3)
print("The current year is", d4)

today = d2
today = int(today)

monthNow = d3
monthNow = str(monthNow)

if monthNow != "10" or monthNow != "11" or monthNow != "12":
    monthNow = str(monthNow[1])
else:
    monthNow = str(monthNow)
#print(monthNow)

yearNow = d4
yearNow = int(yearNow)
#print(calendar.isleap(yearNow))

if calendar.isleap(yearNow):
    print("This is a leap year.")
else:
    print("This year is not a leap year")

days1 = 31
days2 = 30
days3 = 28
days4 = 29
monthLength = 0

# stage 1 - work out the length of the month
if monthNow == str(2) and calendar.isleap(yearNow):
    monthLength = days4
elif monthNow == str(2) and False == calendar.isleap(yearNow):
    monthLength = days3

elif monthNow == str(1) or monthNow == str(3) or monthNow == str(5) or monthNow == str(7) or monthNow == str(8) \
        or monthNow == str(10) or monthNow == str(12):
    monthLength = days1
# elif monthNow == str(4) or monthNow == str(6) or monthNow == str(9) or monthNow == str(11):
else:
    monthLength = days2
print("This month is", monthLength, "days long.")

scrobbles = int(input("How many scrobbles have you listened to so far this month? "))
average = scrobbles / today
rounded = math.floor(average)
print("Your current play average is: ", rounded)

# #Uses the data from the current average to ask what the target is and
# #works out how many tracks need to be listened to
target = int(input("What is your target average? "))
scrobblesNeeded = target * monthLength
print("To achieve that you have to listen to", scrobblesNeeded)
scrobblesToGet = scrobblesNeeded - scrobbles
print("You need to listen to another", scrobblesToGet, "tracks")

# if daysLeft is 0, this prevents a ZeroDivisionError
daysLeft = monthLength - today
print("There are", daysLeft, "days left this month.")

if daysLeft != 0:
    daily = scrobblesToGet / daysLeft
    daily = math.floor(daily)
    print("You need to listen to about", daily, "tracks a day.")
else:
    print("Thank you for using the Average Scrobble calculator.")
print("End")
