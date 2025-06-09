# Python program to print the current date in the given format

import datetime
date = datetime.datetime.now()
print("Current Date and Time",date)

print (date.strftime (" %Y %b %d "))