import math

def calculate_no_of_cans(height, width, cover):
    return math.ceil((height * width) / cover)

width = int(input("Enter the width of the wall: "))
height = int(input("Enter the height of the wall: "))

cover = 5

no_of_cans = calculate_no_of_cans(height = height, width = width, cover = cover)

print(f"You will need {no_of_cans} cans of paint.")