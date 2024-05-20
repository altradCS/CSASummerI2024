minute = int(input("Enter a number of minutes: "))
total_day = minute//(60*24)
total_year = total_day//365
current_day = total_day%365

print(f"{minute} is approximately {total_year} years and {current_day} days")
