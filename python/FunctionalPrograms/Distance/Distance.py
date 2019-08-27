# Write a program Distance.java that takes two integer command-line arguments x and y and 
# prints the Euclidean distance from the point (x, y) to the origin (0, 0). 
# The formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function

import DistanceBL
try:
    x=int(input("enter the x coordinate of the point= "))
    y=int(input("enter the y coordinate of the point= "))
except(TypeError):
    print("valid input needed, string or float inputs not allowed")    
DistanceBL.calculatedistance(x,y)