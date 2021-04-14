heights = input("Enter student height in cms with space seperated: ")
heights_as_list = [int(x.strip()) for x in heights.split(" ")]

total_height = 0
length = 0
for height in heights_as_list:
    length += 1
    total_height += height

print(f"Average heigh is, {round(total_height/length, 2)}")