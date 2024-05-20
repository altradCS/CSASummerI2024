# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes.
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

# Prompt user to enter the minutes in integer
minute = int(input("Enter a minute: "))

# Calculate total number of days from the minutes provided
total_days = minute//(60*24)

# Calculate the number of years from the total days
years = total_days//365

# Calculate the remaining days
remaining_days = total_days % 365

# Display result
print(f"{minute} minutes is approximately {years} years and {remaining_days} days.")
