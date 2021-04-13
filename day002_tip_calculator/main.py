'''
PEMDAS - Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
()
**
* / left to right
+ - left to right
'''

print("Welcome to the Tip calculator.")

currency = "Rs."
total_bill_amount = float(input(f"What was the total bill? {currency} "))
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
no_of_people = input("How many people to split the bill? ")

tip_amount = (total_bill_amount / 100) * float(tip_percentage)
pay_split = round((total_bill_amount + tip_amount) / int(no_of_people), 2)

message = f'''
Total bill amount, {currency} {total_bill_amount}
{tip_percentage} percent of tip, {currency} {tip_amount}
Each person should pay {currency} {pay_split}'''
print(message)
