row_one = ['⬜️', '⬜️', '⬜️']
row_two = ['⬜️', '⬜️', '⬜️']
row_three = ['⬜️', '⬜️', '⬜️']

map = [row_one, row_two, row_three]

print(f"{row_one}\n{row_two}\n{row_three}")

position = input("Where do you want to put the treasure? ")
map[int(position[0])-1][int(position[1])-1] = "X"

print(f"{row_one}\n{row_two}\n{row_three}")