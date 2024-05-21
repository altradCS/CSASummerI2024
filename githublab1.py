# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

current_minute = eval(input('Enter number of minutes: '))

if current_minute <= 0:
    print('Invalid input')
else:
    total_days = current_minute // (24 * 60)
    total_years = total_days // 365
    remaining_days = total_days % 365
    print(f'{current_minute} minutes is approximately {total_years} years and {remaining_days} days') 