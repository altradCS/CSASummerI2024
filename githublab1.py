#prompt the user to input the number of minutes
minutes = int(input("Enter the number of minute(s): "))

#calculate the total number of days from the minutes provided
total_days = minutes//(60*24)

#calculate the number of years from the total dyas
years = total_days//365

#calculate the remaining days after accounting for full years
remaining_days = total_days % 365

#display the result in the format
print(minutes, "is approximately", years, "years and", remaining_days, "days.")
