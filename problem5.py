#!usr/bin/python3

import datetime

name=input("Enter Name :")
now=datetime.datetime.now()
a=now.hour
if a<=12 and a >=5 :
    print("Good Morning...",name)
elif a>=12 and a<=16 :
    print("Good Afternoon...",name)
elif a >=16 and a<21:
    print("Good Evening...",name)
elif a >= 21 :
    print("Good Night...",name)

