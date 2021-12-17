#import datetime
from datetime import date

#get name and age from user
name = input("Enter your name : ")
age = int(input("Enter your age: "))

#calculating age difference
age_diff = 100 - age

#getting the current year
today = date.today().strftime("%Y")

#finding the 100th year ot he user
will_turn_100 = age_diff + int(today)

print('Hello '+name+', you will turn 100 in '+str(will_turn_100)+'A.D.')
