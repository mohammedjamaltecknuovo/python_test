import sys

milkshakes = {
    "vanilla": 2.99,
    "chocolate": 3.50,
    "strawberry": 3.75,
    "mint": 3.25
} # Menu with flavours and prices

names = list(milkshakes.keys()) # List of names used to map numbers to flavours

print("Welcome to the Milk Bar!")

budget = 20.0 # Starting money

while budget <= 0: # Protect against bad input for budget
    print("Budget must be a positive number.")

min_price = min(milkshakes.values()) # Cheapest drink used to control the loop

while budget > min_price: # Main loop, runs while Sam can still afford something

    for index, milkshake in enumerate(milkshakes, start=1): # Show menu each round
        print(f"{index}. {milkshake}. {milkshakes[milkshake]}")

    input_choice = int(input("Enter the number of the milkshake you want to buy (or 0 to exit): ")) # Read choice from user

    if input_choice == 0: # Exit option
        sys.exit("Thank you for visiting the Milk Bar!")

    if input_choice < 1 or input_choice > len(names): # Check if input is in range
        print("Please choose a valid milkshake number.")
        continue

    selected_name = names[input_choice - 1] # Convert menu number to real flavour name

    price = milkshakes[selected_name] # Find price

    if price > budget:
        print("You cannot afford this drink. The barman throws you out.") # Check if Sam can afford it
        sys.exit()

    budget = budget - price # Subtract price from budget

    print(f"You bought a {selected_name} milkshake for {price}.") # Show new budget
    print(f"Your remaining budget is {budget}.\n")

print("You do not have enough money for any drink.") # If loop ends, Sam cannot buy anything else