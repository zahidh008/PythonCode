# Import library for arduino code

import json



#Read data form wifi
# weather report// control value// 



#Write data to wifi
#Control value// Sensor value



#Read data form GSM
#call and sms



#Write data to GSM
#call and sms



#Read data from sensors


alarm = """
{
    "sun": ["05:40","05:50"],
    "mon": ["05:40","05:50"],
    "tue": ["05:40","05:50"],
    "wed": ["05:40","05:50"],
    "thr": ["05:40","05:50"]
    }
"""
alarm = json.loads(alarm)


#Routine
#Morning
#Alarm based on the day
entry = {'carl': 33}
alarm['sun'].append(entry)
print(alarm)
print("Alarm ringing")






