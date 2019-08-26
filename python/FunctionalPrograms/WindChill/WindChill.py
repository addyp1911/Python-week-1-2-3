# Write a program WindChill.py that takes two double command-line arguments t and v and prints the wind chill. 
# Use Math.pow(a, b) to compute ab. 
#Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
# the National Weather Service defines the effective temperature (the wind chill) to be:
#Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3 

import WindChillBL 
temp=float(input("enter the temperature in fahrenheit"))
windspeed=float(input("enter the windspeed in miles per hour"))
   
WindChillBL.disp(temp,windspeed)
