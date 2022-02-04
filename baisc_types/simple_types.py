# variables are "boxes" you can put data in to create a variable, we use `=`
# this means what is on the right of the of the equal sign will be st inside the
# variable on the left.

# there are several types of data you can set to your variables
# strings represent text
my_string = "hello world"

# ints are for integer numbers (nombres entier)
my_int = 42

# floats are for floating point numbers (nombres a virgules)
my_float = 0.42


# FUNCTIONS

# a function is a statement that will "do something"
# it is a way to (re)use tools developed by ourselves and other.
# we use the name of the function followed by parenthesis
# we put the input(s) of the function between those parenthesis.

# one of such functions is the print function. This function
# shows its input to the user

# the folowing statement will show the famous hello world:
print("hello world")

# since the "hello world" string is already assigned to
# the `my_string` variable we can use it directly to print
# the same message
print(my_string)

# similarly, we can print the values of all our variables
print(my_int)
print(my_float)


# OPERATIONS

# we can use math to change our variables
# and see the result

new_value = my_int - 5
print(new_value, type(new_value))
new_value = my_int + my_float
print(new_value, type(new_value))
new_value = my_int * 5
print(new_value, type(new_value))

# // means euclidian division
new_value = my_int // 5
print(new_value, type(new_value))
# % is the modulo operations (the remainder of an euclidian division)
new_value = my_int % 5
print(new_value, type(new_value))
# note: in the above section of the code we use the `type` function that will
# return the type of a specific variable

# the input function will show it's input as a message and ask for the user to
# type something and then hit enter. It will return the user's input
# user_input = input("what is your name")
print("hello ", user_input)


# EXERCISE:
# what do you think will happen?
# for each of the following statements, try to guess what will happen
# and then uncomment (remove the #) and see if you guessed rigth

# print(my_int + my_float)
# print(type(my_float + my_int))
# print(type(my_int + my_float))
# print(my_string + my_string)
# print(my_string + my_float)
# print(type(input("give some value punny human")))
# print(type(type(my_float)))
# print(type(input))
