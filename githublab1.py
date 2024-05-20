# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
minute = input("Enter the minutes: ")

#Convert String to integer
input_minute = int(minute)
# Calculate day from user_input_minute

total_day = input_minute // (60 * 24)

#calculate the number of year from total days

total_year = total_day // 365

#calculate the remaining days after accounting for full years:
remaining_days = total_day % 365

print(f"{input_minute} minutes is approximately {total_year} years and {remaining_days} days")
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
