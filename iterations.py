# TASK:
#loop to get 5 names as inputs + prints with "is awesome" added to it. 

#while loop
#for loop
#list comp
#STRETCH GOAL: list comp one line only! 

# inner 
# [input("Enter name: ") + " is awesome" for n in range(5)]

# outer
# [print(f"y is awesome")for y in iterable]

x = [print(f"{y} is awesome") for y in [input("Enter name: ") for n in range(5)]]

print(x)