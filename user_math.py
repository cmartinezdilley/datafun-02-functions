"""
Module 2 Task 3- Christine Martinez 24Jan2023
Functions that are related to cats. 

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = 0 # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

def blackcat_avg(*blackcat):
    """Return the number of black cats in each room of the shelter"""
    return sum(blackcat)/len(blackcat)

def cost_of_cat_food_per_room(friskies_cost, room_count):
    """Returns the cost of friskies for each room in the cat shelter"""
    return math.prod([friskies_cost*room_count])

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1)={math.comb(5,1)}")
    print(f"math.perm(5,1)=math{math,math.perm(5,1)}")

    print(f"Average number of black cats= {blackcat_avg(5,6,7,8)}")
    print()
    print(f"Cost of cat food={cost_of_cat_food_per_room(20,30)}")
    