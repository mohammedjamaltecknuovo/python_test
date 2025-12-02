# # # # # # repeatability + abstraction 

# # # # # def greet(name, age): #parameters - pass through name first then age
# # # # #     print(f"Hello, {name} aged: {age}.") # use as variables inside the function

# # # # # greet("c", 20) 

# # # # # def greet(first, last, age=30): #parameters - pass through name first then age positionally
# # # # #     print(f"Hello, {first} {last} aged: {age}.")

# # # # # greet() 

# # # # # *args 
# # # # # if we dont know how many arguments need to be passed through positionaly. passed as a tuple.

# # # # # def make_pizza(size, *toppings): 
# # # # #     print(f"Order for {size} pizza, with the following toppings:")
# # # # #     for topping in toppings:
# # # # #         print(topping)

# # # # # make_pizza("large", "mushrooms", "sweetcorn")

# # # # # **kwargs
# # # # # if we dont know how many arguments need to be passed through keyword. passed as a dictionary

# # # # # def order(**stuff):
# # # # #     print("Order:")
# # # # #     for key, value in stuff.items():
# # # # #         print(f"{key}: {value}")

# # # # # order(main="pasta", drink="cola", side="fries")

# # # # # def combined(*args, **kwargs):
# # # # #     print(args)
# # # # #     print(kwargs)

# # # # # combined(1, 2, b=3, a=4) 

# # # # # / * - control positional and keyword arguments
# # # # # all args before / must be positional
# # # # # all args after * must be keyword
# # # # # enforce positional or keyword only

# # # # def example(a, b, /, *, c, d): 
# # # #     print(f"a: {a} b: {b} c: {c} d: {d}")
          
# # # # example(1, 2, c=3, d=4)

# # # def maths_ops(a, b, /, operation="add", *, decimal_place=None): 
# # #     if operation == "add":  
# # #         result = a + b
# # #     elif operation == "subtract":
# # #         result = a - b
# # #     else:
# # #         raise TypeError("Only 'add' or 'subtract' please!")
# # #     return round(result , decimal_place)

# # # print(maths_ops(2,5))
# # # print(maths_ops(2,5, operation="add"))
# # # print(maths_ops(2,5, operation="subtract")) 
# # # print(maths_ops(2,5, operation="subtract", decimal_place=2))
    
# # # Recursion, lambdas, wrappers, functools, higher-levels.

# # # Recursion - function that calls itself until a base case is reached:

# # # def factorial(n):
# # #     if n == 1:
# # #         return 1
# # #     else:
# # #        return n * factorial(n - 1)

# # # print(factorial(5))  

# # # Frame: 
# # #     - stores each function call
# # #     - holds locals(), globals().
# # #     - code object(f_code) (function code)
# # #     - calling context 

# # # stack: 
# # #     - stack of frames, ordered from recent to oldest.
# # #     - pops the functions (deletes + returns it's return statement) when it ends.

# # import inspect

# # def test_function():
# #     print("name: ", inspect.currentframe.f_code.co_name)
# #     print("stack: ", inspect.stack()[0].function) 
# #     x = "hello"
# #     print(locals())
# #     for f in inspect.stack():
# #         print(f.function)

# # def call():
# #     test_function()

# # call()
# # print(locals())
# # print(locals() == globals())

# # lambdas: descrete unnamed functions. 

# lambda args : expression (iterables)   

# add_function = lambda x, y: x + y

# print(add_function(2, 3))

# numbers = [1, 2, 3, 4, 5]   
# squared = map(lambda x: x**2, numbers)

# print(list(squared)) 

