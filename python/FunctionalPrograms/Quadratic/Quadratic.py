# Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c. 
# Since the equation is x*x, hence there are 2 roots. 
# The 2 roots of the equation can be found using a formula 
#delta = b*b - 4*a*c
#Root 1 of x = (-b + sqrt(delta))/(2*a)
#Root 2 of x = (-b - sqrt(delta))/(2*a)
#Take a, b and c as input values to find the roots of x.

    
import QuadraticBL
print("we are goin to print the quadratic equation of the order a*x*x+ b*x+c")
a=int(input("enter the value of a= "))
b=int(input("enter the value of b= "))
c=int(input("enter the value of c= "))

QuadraticBL.roots(a,b,c)