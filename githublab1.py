# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

ask_user = int(input("Enter the minutes: "))

total_day = ask_user / (60 * 24)

years = total_day // 365


remaining_days = total_day % 365

print(f"{ask_user} minutes is approximately {years:.0f} years and {remaining_days:.0f} days.")    