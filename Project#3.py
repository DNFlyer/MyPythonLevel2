import datetime as dt #yes
import time

print("Oh hey there!")
print("Looks like someone is excited about their birthday!")
print("Well, you've come to the right place!")
print("Let's find out how long until your next birthday!")

#B'Day Entry by user
while True:
    try:
        year = int(input("Enter your birth year (YYYY): "))
        month = int(input("Enter your birth month (MM): "))
        day = int(input("Enter your birth day (DD): "))

        #Special Rejections :) - In-case user enters a future date
        if year > dt.datetime.now().year:
            raise ValueError("Seems like we got a time traveler in our midst! \nWell, unfortunately, you aren't supposed to be born yet \nPlease go back to your own time.....")

        #Format
        birth_date = dt.datetime(year, month, day)
        break

    except ValueError as huh:
        print(f"Invalid input: {huh}. Please try again.\n")

#Day of the week
print("\nCool! You were born on a", birth_date.strftime("%A"))

#Next B'Day when?
today = dt.datetime.now()

#This year?
try:
    this_year_birthday = dt.datetime(today.year, month, day)
except ValueError:
    #Feb 29th!! Shift to March 1st for non-leap years
    this_year_birthday = dt.datetime(today.year, 3, 1)

#Oh, nvm... It's next year...
if this_year_birthday < today:
    try:
        next_birthday = dt.datetime(today.year + 1, month, day)
    except ValueError:
        #Check if leap year for Feb 29th, else shift to March 1st
        next_birthday = dt.datetime(today.year + 1, 3, 1)
else:
    next_birthday = this_year_birthday

#Handling them exception :)

print("So your next birthday would be on", next_birthday.strftime("%A, %d %B %Y"))
print("\nHere goes the countdown!!!")
time.sleep(1)

#Countdown loop
while True:
    now = dt.datetime.now()
    diff_seconds = int(next_birthday.timestamp() - now.timestamp())

    if diff_seconds <= 0: #Countdown complete ;)
        print("\nHappy Birthday comrade!")
        break
        
    #Floor Division, simply lovely!
    days = diff_seconds // (24 * 3600)
    hours = (diff_seconds % (24 * 3600)) // 3600
    minutes = (diff_seconds % 3600) // 60
    seconds = diff_seconds % 60

    print(f"Time left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="\r")
    
    # Sleepy-time
    time.sleep(1)

#Before was was was, was was is