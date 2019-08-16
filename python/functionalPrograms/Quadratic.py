# Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c. 
# Since the equation is x*x, hence there are 2 roots. 
# The 2 roots of the equation can be found using a formula 
#delta = b*b - 4*a*c
#Root 1 of x = (-b + sqrt(delta))/(2*a)
#Root 2 of x = (-b - sqrt(delta))/(2*a)
#Take a, b and c as input values to find the roots of x.
class Quadratic:
    def calculateRoots():
        print("we are goin to print the quadratic equation of the order a*x*x+ b*x+c")
        a=int(input("enter the value of a= "))
        b=int(input("enter the value of b= "))
        c=int(input("enter the value of c= "))
        delta=b*b-4*a*c
        print("the first root of the equation is =")
        x1=(-b+pow(delta,0.5))/2*a
        print(x1)
        print("the second root of the equation is =")
        x2=(b+pow(delta,0.5))/2*a
        print(x2)


#driver code
    calculateRoots()