year = int(input("Enter year: "))
leap_year = False

if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True

if leap_year:
    print(f"Year {year} is leap year.")
else:
    print(f"Year {year} is not a leap year.")