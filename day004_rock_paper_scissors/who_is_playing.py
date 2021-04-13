import random

name_as_string = input("Enter names with comma seperated: ")
names_list = [x.strip() for x in name_as_string.split(",")]

random_index = random.randrange(len(names_list))

print(f"{names_list[random_index]} is going to buy the meal today!")