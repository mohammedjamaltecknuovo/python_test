# budget = 20 # Starting money

# milkshakes = {
#     "1": (3, "Strawberry"),
#     "2": (4, "Chocolate"),
#     "3": (5, "Vanilla")
# } # Menu with flavours and prices

# while True:
#     print("Drinks Menu:")
#     for option, (price, flavor) in milkshakes.items():
#         print(f"{option}. {flavor} - ${price}")

#     choice = input("Enter your choice of drink? ")

#     if choice not in milkshakes:
#         print("Invalid choice.")
#         continue

#     if choice.upper() == "Q":
#         print("Exiting the program.")
#         break

#     price, flavour = milkshakes[choice]
#     if price > budget:
#         print("You cannot afford this drink. The barman throws you out.")
#         break

#     print(f"Enjoy {flavour} milkshake.")
#     budget -= price
#     print(f"Remaining budget: ${budget}")

from typing import Dict

budget = 20.0  

Menu = Dict[str, tuple[int, str]] # type alias - capitalised to show not a variable
                                  # no effect - python doen't enforce types ever
                                  # mypy is a static tool to check - best implemented in 
                                  # a static code analysis pipeline
                                  # updates to the structure propagate through all updates.

milkshakes = {
    "1": (3, "Strawberry"),
    "2": (4, "Chocolate"),
    "3": (5, "Vanilla")
} 

while True:
    print("Drinks Menu:")
    for option, (price, flavor) in milkshakes.items():
        print(f"{option}. {flavor} - ${price}")

    choice = input("Enter your choice of drink? ")

    if choice not in milkshakes:
        print("Invalid choice.")
        continue

    if choice.upper() == "Q":
        print("Exiting the program.")
        break

    price, flavour = milkshakes[choice]
    if price > budget:
        print("You cannot afford this drink. The barman throws you out.")
        break

    print(f"Enjoy {flavour} milkshake.")
    budget -= price
    print(f"Remaining budget: ${budget}")