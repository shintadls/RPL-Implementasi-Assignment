from datetime import datetime
from datetime import time
import string 

dt_now = datetime.now()
star = datetime.strptime('2022-10-20 08:00:00', '%Y-%m-%d %H:%M:%S')
end = datetime.strptime('2022-10-20 17:00:00', '%Y-%m-%d %H:%M:%S')
Basefee = 0
Addfee = 0
drop = string

x = int(input('Please enter the amount of computer: '))
if (x == 1 or x == 2):
    Basefee+= 50
    Addfee = 0
elif (x >= 3 and x <= 10):
    Basefee+= 50 
    for i in range(0,x):
        Addfee += 10
elif (x >10):
    Basefee+= 500
    for i in range(0,x):
        Addfee += 10
if (dt_now < star and dt_now > end):
    Basefee = Basefee * 2
drop = input("Are you willing to drop off and pick up type (yes): " )
if (drop == "yes"):
    Basefee = Basefee / 2

print("Total fee : ",Basefee + Addfee)