minute = int(input("Enter a minute: "))
total_days = minute/(60*24)
years = total_days/365
remaining_days = total_days % 365
print(minute, "minutes", "is approximately", years, "years", "and", remaining_days, "days")

