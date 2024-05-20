# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days


# Step 1: Prompt the user to input the number of minutes.
minutes_input = input("Enter the number of minutes: ")

# Step 2: Convert the string to an integer.
minutes = int(minutes_input)

# Step 3: Calculate the total number of days from the minutes provided.
# There are 60 minutes in an hour and 24 hours in a day.
total_days = minutes / (60 * 24)

# Step 4: Calculate the number of years from the total days.
# Assume a year has 365 days.
years = int(total_days // 365)

# Step 5: Calculate the remaining days after accounting for full years.
remaining_days = int(total_days % 365)

# Step 6: Display the result in the format
print(f"{minutes} minutes is approximately {years} years and {remaining_days} days.")