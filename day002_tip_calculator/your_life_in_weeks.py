# Simple program to convert remain years into days, weeks, months
# Human life is 90 years
# Assumption years would just have 365 days always

current_age = input("Enter your current age:\n")
remaining_years = 90 - int(current_age)

remaining_years_in_weeks = remaining_years * 52
remaining_years_in_months = remaining_years * 12
remaining_years_in_days = remaining_years * 365

message = f"You have {remaining_years_in_days} days, {remaining_years_in_weeks} weeks, and {remaining_years_in_months} months left."
print(message)
