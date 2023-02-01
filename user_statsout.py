(base) iMac:datafun-02-functions-1 nistine$ /usr/bin/python3 /Users/nistine/Documents/datafun-02-functions-1/user_stats.py
The mode of the agility scores is 111.
The mean of the agility scores is 99.12.
The median of the agility scores is 102.5.
The variance of the agility scores is 179.25. 
The standard deviation of the agility scores is 13.39. 
Traceback (most recent call last):
  File "/Users/nistine/Documents/datafun-02-functions-1/user_stats.py", line 97, in <module>
    slope, intercept = statistics.linear_regression(x_times, y_temps)
AttributeError: module 'statistics' has no attribute 'linear_regression'