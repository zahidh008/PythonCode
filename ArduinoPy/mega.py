# Import library for arduino code

import json



#Read data form wifi
# weather report// control value// 



#Write data to wifi
#Control value// Sensor value



#Read data form GSM
#call and sms
textcomands = ["show command", "status", "led on", "led off", "fan on", "fan off"]
text = ["show command", "status", "led on", "led off"]
receivedsms = "show all command"
receivedsms = receivedsms.lower()

for a in textcomands:
    b = a.split(' ')
    for c in b:
        if receivedsms.find(c) != -1:
            match = 1
        else:
            match = 0
            break
    if match == 1:
        print("Matched. Execute- ")
        # print(a)
        if a == "show command":
            print("Commands are: ")
            for a in textcomands:
                print(a)
        elif a == "status":
            print("status")
        elif a == "led on":
            print("led on")
        elif a == "led off":
            print("led off")
        elif a == "fan on":
            print("fan on")
        elif a == "fan off":
            print("fan off")
        
        


# if receivedsms.find('STATUS') != -1:
#     print("show status") #show status


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






