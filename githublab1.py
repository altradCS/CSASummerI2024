# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
minutes = int(input("Enter the number of minutes: "))
years = minutes // (60 * 24 * 365)
remaining_minutes = minutes % (60 * 24 * 365)
days = remaining_minutes // (60 * 24)
print(f"{minutes} minutes is approximately {years} years and {days} days.")
