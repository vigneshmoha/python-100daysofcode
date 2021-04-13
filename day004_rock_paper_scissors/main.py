import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''

options = [rock, paper, scissors]
computer_option_index = random.randrange(len(options))

user_option_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

print(f"Your option: {options[user_option_index]}\nComputer option:\n{options[computer_option_index]}\n")

if user_option_index >= 3 or user_option_index < 0:
    print("Invalid option. You lose!")
elif user_option_index == computer_option_index:
    print("It is a draw!")
else:
    if ((user_option_index == 0 and computer_option_index == 2) 
        or (user_option_index == 2 and computer_option_index == 1) 
        or (user_option_index == 1 and computer_option_index == 0)):
        print("You won!")
    else:
        print("You lose!")
