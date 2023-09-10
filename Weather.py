import requests
import pandas as pd

import time as t
import math as m
import smtplib as smt

sender_email = "*************@gmail.com"
rec_email = []
#print(t.localtime().tm_hour > 7 and t.localtime().tm_hour < 22)
time_of_day = ["morning", "afternoon", "evening"]
day_temp = ['morn', 'day', 'eve']

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

Subject = "Weather Update"

print(t.localtime())
n = 0
while (n == 0):
    if (t.localtime().tm_hour >= 7 and t.localtime().tm_hour <= 22):
        
        time_of_day_index = int()
        if (t.localtime().tm_hour < 11):
            time_of_day_index = 0
        elif (t.localtime().tm_hour < 18):
            time_of_day_index = 1
        elif (t.localtime().tm_hour < 22):
            time_of_day_index = 2
        
        r = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=43.65&lon=-79.34&exclude=&appid=********************")
        print(r.text)
        # Weather data
        weather_desc = r.json()["current"]["weather"][0]["description"]
        temp_real_current = m.floor(((r.json()['current']['temp'] - 273.15) * 100) / 100)
        temp_feels_current = m.floor(((r.json()['current']['feels_like'] - 273.15) * 100) / 100)
        humidity = r.json()['current']['humidity']
        uv_current = m.floor(r.json()['current']['uvi'] * 100) / 100
        pop_now = r.json()['hourly'][1]['pop'] * 100
        
        temp_max = m.floor(((r.json()['daily'][0]['temp']['max'] - 273.15) * 100) / 100)
        temp_min = m.floor(((r.json()['daily'][0]['temp']['min'] - 273.15) * 100) / 100)
        uv_max = m.floor(r.json()['daily'][1]['uvi'] * 100) / 100
        
        if (time_of_day_index != 2):
            temp_real_later = m.floor(((r.json()['daily'][0]['temp'][day_temp[time_of_day_index + 1]] - 273.15) * 100) / 100)
            temp_feels_later = m.floor(((r.json()['daily'][0]['feels_like'][day_temp[time_of_day_index + 1]] - 273.15) * 100) / 100)
        
        pop_daily = r.json()['daily'][0]['rain']
        rain_daily = r.json()['daily'][0]['rain']
        
        weather_id = r.json()['current']['weather'][0]['id']

        week_days[t.localtime().tm_wday]
        
        Subject = "Weather Update %s: %s" %(week_days[t.localtime().tm_wday], str(t.localtime().tm_hour) + ":" + str(t.localtime().tm_min) + ":" + str(t.localtime().tm_sec))
        
        
        
        if (weather_id <= 800):
            email_body = "This %s in there is a %s in *****. " %(time_of_day[time_of_day_index], weather_desc)
        else:
            email_body = "This %s in there are %s in *****.. " %(time_of_day[time_of_day_index], weather_desc)
        
        if (temp_real_current != temp_feels_current):
            email_body += "It is %s degrees " %(str(temp_real_current))
            email_body += "and it feels like %s " %(str(temp_feels_current))
        else:
            email_body += "It is %s degrees " %(str(temp_real_current))
        email_body += "with a humidity of %s%s." %(str(humidity), "%")
        
        if (temp_max != temp_real_current):
            email_body += "\nThe temperature will reach a high of to %s degrees " %(str(temp_max))
            email_body += "and a low of %s." %(str(temp_min))
        else:
            email_body += "\nThe tempuratue is at its peak now and will reach a low of %s degrees." %(str(temp_min))

        if (uv_current != 0 and uv_current <= uv_max):
            email_body += "\nThe current UV index is %s (the UV index will reach a maximum of %s)." %(uv_current, str(uv_max))
        else:
            email_body += "\nThe current UV index is %s." %(uv_current)

        if (pop_now > 0):
            email_body += "\nThere is a %s%s chance of rain in the next hour" %(str(pop_now), "%")

        if (time_of_day_index != 2):
            email_body += "\n\nThis %s:" %(time_of_day[time_of_day_index + 1])
            email_body += "\nThe temperature will be %s degrees" %(str(temp_real_later))
            email_body += "\nand it will feel like %s degrees" %(str(temp_feels_later))

        email_body += "\n"

        if (pop_daily > 15):
            email_body += "\nThere is a %s%s chance of rain today" %(str(pop_daily), "%")
            email_body += "\nand there could be %smm of rain." %(str(rain_daily))
        else:
            email_body += "\nIt probably won't rain today."
            
        
        message = 'Subject: %s\n\n%s' %(Subject, email_body)
        
        server = smt.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, "*************")
        print("logged in")
        for email in rec_email:
            server.sendmail(sender_email, email, message)
            print("sent to " + email)
            
        #server.sendmail(sender_email, rec_email, message)
        print("done\n")

        print (message)
    #t.sleep((3.5) * 3600 - 5)
    n += 1
    
