#!usr/bin/python3

import datetime


name=input("Enter your name :  ")
age=int(input("Enter your age :  "))

cal=datetime.datetime.now().year+(95-age)

print("You will be/was turn to 95 in year: ",cal)

