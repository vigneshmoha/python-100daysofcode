scores = input("Enter student scores with space seperated: ")
scores_as_list = [int(x.strip()) for x in scores.split(" ")]

# Two approach
# 1. Visit every element to compate and identify which is highest
# 2. Sort the list and get the last element by index -1

max_score = 0
for score in scores_as_list:
    if max_score < score:
        max_score = score

print(f"Approach 1: Heighest score is {max_score}")

scores_as_list.sort()
print(f"Approach 2: Heighest score is {scores_as_list[-1]}")