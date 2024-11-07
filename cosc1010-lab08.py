# Koen Myers
# UWYO COSC 1010
# 11/6/2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to: (Google, "how to make something a float in python" 11/5/2024), 
#(https://www.w3schools.com/python/ref_string_count.asp, "how to count how many decibels are in a string python", 11/6/2024)
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def check_numbers(strin):
    """How to check a number"""
    if "." in strin:
        return float(strin)
    elif strin.isdigit():
        return int(strin)
    else:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(z,f,low,upp):
    end_value=[]
    if low >= upp:
        return print('Invalid Inputs')
    for x in range(low, upp + 1):
        y=z*x+f
        end_value.append(y)
    return end_value

while True:
    numbers_give=input("Input values for Line (m b lower upper)= ")
    if numbers_give.lower() == "exit":
        break
    m=0
    b=0
    lower=0
    upper=0
    numbers=numbers_give.split()
    if len(numbers) != 4:
        print("Invalid Inputs")
        continue
    ms= numbers[0]
    bs=numbers[1]
    lowers=numbers[2]
    uppers=numbers[3]
    if check_numbers(ms) != False:
        m=check_numbers(ms)
    else:
        print('Invalid Input')
        break
    if check_numbers(bs) != False:
        b=check_numbers(bs)
    else:
        print('Invalid Input')
        break
    if check_numbers(lowers) != False:
        lower=check_numbers(lowers)
    else:
        print('Invalid Input')
        break
    if check_numbers(uppers) != False:
        upper=check_numbers(uppers)
    else:
        print('Invalid Input')
        break
    print(slope_intercept(m,b,lower,upper))

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
