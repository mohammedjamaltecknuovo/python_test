# if , else , else if (elif) 
# basic_syntax = 
# if condition is True:
# block of code to Run 
# else: 
# block of code if the if was false.

on_holiday = True # boolean variable
is_admin = False
is_verified = False

if (is_admin or is_verified) and not on_holiday:
    print("Access allowed")
else:
    print("Access denied")