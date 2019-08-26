
# ----------------------------------Quadratic prg-----------------------------------------------
# Quadratic.py
# date : 26/08/2019
# method to find and print the roots of the equation a*x*x + b*x + c. 

def roots(a,b,c):

    delta=b*b-4*a*c                         # quadratic formula is implemented to find the roots
    print("the first root of the equation is = ")
    root1=(-b+pow(delta,0.5))/2*a
    print(root1)
    print("the second root of the equation is = ")
    root2=(root1 + pow(delta,0.5))/ 2*a
    print(root2)
 