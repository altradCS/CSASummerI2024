# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

# prompt for input
minutes = int(input("Enter your minutes: "))

# Calculate the total number of days:
total_day = minutes/(60*24)

# Calculate the number of years:
total_year = int(total_day/365)

# Calculate remainder:
remain = int(total_day%365)

# Display the result.
print(f"{minutes} minutes is approximately {total_year} years and {remain} days")