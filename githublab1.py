# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

# Prompt the user to input the number of minutes
minutes_input = input("Enter the number of minutes: ")

# Convert the input to an integer
minutes = int(minutes_input)

# Calculate the total number of days from the minutes provided
total_days = minutes / (60 * 24)

# Calculate the number of years from the total days
years = total_days // 365

# Calculate the remaining days after accounting for full years
remaining_days = total_days % 365

# Display the result
print(f"{minutes} minutes is approximately {int(years)} years and {int(remaining_days)} days.")
