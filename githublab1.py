# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days


minutes = int(input("Enter your minutes: "))
# Calculate the total number of days from the minutes provided:
total_day = minutes/(60*24)
# Calculate the number of years from the total days:
total_year = int(total_day/365)

# Calculate the remaining days after accounting for full years:
Remaining_days = int(total_day%365)


# Display the result in the format: "XXXX minutes is approximately Y years and Z days".
print("{} minutes is approximately {} years and {} days".format(minutes, total_year,Remaining_days))

