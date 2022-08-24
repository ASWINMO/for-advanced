import time
import datetime
print("current date and time:",datetime.datetime.now())
print("Current year:",datetime.date.today().strftime("%Y"))
print("Month of year:",datetime.date.today().strftime("%B"))
print("Week number of the year:",datetime.date.today().strftime("%W"))
print("Week number of the week:",datetime.date.today().strftime("%w"))
print("Day of year:",datetime.date.today().strftime("%j"))
print("day of the month:",datetime.date.today().strftime("%d"))
print("day of week:",datetime.date.today().strftime("%A"))
