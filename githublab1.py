# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
# prompt the user to input the number of minutes
minutes = input("Enter number of minutes: ")

minutes = eval(minutes)

total_minutes_of_Days = minutes/60/24

year = total_minutes_of_Days/365

remaining_days = total_minutes_of_Days % 365

print(f"{minutes} minutes is approximately {year:.0f} years and {total_minutes_of_Days:.0f} days")
