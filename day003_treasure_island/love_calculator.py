name_one = input("Enter name of the person 1: ")
name_two = input("Enter name of the person 2: ")

first_digit_score = 0
second_digit_score = 0

true_chars = ['T','R','U','E']
love_chars = ['L','O','V','E']

for c in true_chars:
    first_digit_score += name_one.upper().count(c)
    first_digit_score += name_two.upper().count(c)
for c in love_chars:
    second_digit_score += name_one.upper().count(c)
    second_digit_score += name_two.upper().count(c)

score = int(f"{first_digit_score}{second_digit_score}")

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")