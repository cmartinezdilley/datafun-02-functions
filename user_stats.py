"""
Task 4- Module 2
Christine Martinez
This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]


# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

#Calculate the agility scores
mode= statistics.mode(scores)
mean= statistics.mean(scores)
median= statistics.median(scores)
variance= statistics.variance(scores)
standard_deviation=statistics.stdev(scores)

print(f"The mode of the agility scores is {mode}.")
print(f"The mean of the agility scores is {mean}.")
print(f"The median of the agility scores is {median}.")
print(f"The variance of the agility scores is {variance:.2f}. ")
print(f"The standard deviation of the agility scores is {standard_deviation:.2f}. ")

slope, intercept = statistics.linear_regression(x_times, y_temps)

print(f"""The best fit line has a slope of {round(slope,2)} and intercept of {round(intercept, 2)}.""")

#Slope and intercept- predicting the temp
future_x=13
future_y= slope*future_x+intercept
print(f"""The temp at hour 13 will be {round(future_y,0)} degrees.""")
