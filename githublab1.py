# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
minute = int(input("Enter the minutes"))
totalDays = minute/(60*24)
totalYears = round(totalDays/365)
remainingDays = round(totalDays%365)
print(minute, "minutes is approximately", totalYears, "years and" ,remainingDays, "days")
