# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
minute = int(input("Enter a number of minutes: "))
total_day = minute//(60*24)
total_year = total_day//365
current_day = total_day%365

print(f"{minute} is approximately {total_year} years and {current_day} days")