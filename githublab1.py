# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

num_min = (input("Enter the number of minutes: "))
num_min = int(num_min)

total_day = num_min // (60 * 24)
total_year = total_day // 365
remain_day = total_day % 365

print(f"{num_min} minutes is approximately {total_year} years and {remain_day} days.")

