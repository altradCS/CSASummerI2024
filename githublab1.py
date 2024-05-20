# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

minute = int(input("Enter minute: "))

total_day = minute / (60 * 24)
total_year = int(total_day / 365)
remain_day = int(total_day % 365)

print(f"{minute} minutes is approximately {total_year} years and {remain_day} days.")

