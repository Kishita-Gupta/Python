#!usr/bin/python3

import os


def checkDigit(username):
    return any(char.isdigit() for char in username )


username=input('Enter String :')
if not checkDigit(username):
    password="hello"+username
    a="useradd -p $(openssl passwd -1 "+password+") "+username
    os.system(a)

else:
  print("No User create")

