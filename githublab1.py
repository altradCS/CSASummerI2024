# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
#chanra levis
print ("Insert time in minutes.")
inputuser = int(input("HERE "))
number_of_minutes = inputuser
if (number_of_minutes <= 60):
    print (number_of_minutes ,"minutes")
number_of_hours = number_of_minutes / 60
if (number_of_hours > 1 and number_of_hours < 24):
    print (number_of_hours ,"hours")
number_of_days  = number_of_hours / 24
if (number_of_days > 1 and number_of_days < 365):
    print (number_of_days ,"days")
number_of_years = number_of_days / 365
number_remainingdays = number_of_days%365
print (inputuser ,"minutes is approximately" ,number_of_years ,"and ", number_remainingdays ,"days")
