# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

Minutes = input("Enter the number of minutes:")
Minutes =  int(Minutes)
day = Minutes/60/24
year = day/365
remaining_day =  day % 365

print(f'{Minutes} minutes is approximately {year:.0f} year(s) and {remaining_day:.0f} days')