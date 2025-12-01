# print("Rectangle Program")

# length_text = input("Enter the length of the rectangle: ")
# print("Raw input (text):", length_text) # length_text holds a string like "10"

# length = int(length_text) # this will convert text to integer
#                          # int(length_text) converts "10" to integar 10 -> after the conversion the program can do arithmetic with length
# print("Length as number:", length) 

print("Rectangle Program")

# Input length
length = int(input("Enter the length of the rectangle: "))
print("Length as number:", length)

# Input width
width = int(input("Enter the width of the rectangle: "))
print("Width as number:", width)    

# Calculate perimeter
perimeter = 2 * length + 2 * width

# Calculate area
area = length * width 

# Output results
print("Perimeter of the rectangle is:", perimeter)
print("Area of the rectangle is:", area)    

