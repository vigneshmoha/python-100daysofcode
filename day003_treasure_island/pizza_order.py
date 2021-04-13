currency = "$"
small_pizza = 15
medium_pizza = 20
large_pizza = 25
extra_pepperoni_small = 2
extra_pepperoni_medium_large = 3
extra_cheese = 1

print(f'''
Welcome to Python Pizzeria
**************************
Pizza Menu
**********
* Small Pizza: {currency}{small_pizza}
* Medium Pizza: {currency}{medium_pizza}
* Large Pizza: {currency}{large_pizza}
* Extra Pepperoni (Small pizza): +{currency}{extra_pepperoni_small}
* Extra Pepperoni (Medium/Large Pizzas): +{currency}{extra_pepperoni_medium_large}
* Extra cheese (Any size): +{currency}{extra_cheese}
''')

size = input("Enter the pizza size(S/M/L): ")
add_extra_pepperoni = input("Do you want toadd extra pepperoni? Please enter (Y/N): ")
add_extra_cheese = input("Do you want toadd extra cheese? Please enter (Y/N): ")

amount = 0

if add_extra_cheese == "Y":
    amount += 1

if size == "S":
    amount += small_pizza
elif size == "M":
    amount += medium_pizza
else:
    amount += large_pizza

if add_extra_pepperoni == "Y":
    if size == "S":
        amount += extra_pepperoni_small
    else:
        amount += extra_pepperoni_medium_large

print(f"You final bill is {currency}{amount}.")
