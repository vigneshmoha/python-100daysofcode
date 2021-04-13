given_number = input("Please enter a number: ")
odd_or_even = "odd"
if int(given_number) % 2 == 0:
    odd_or_even = "even"

message = f"{given_number} is an {odd_or_even} number."
print(message)