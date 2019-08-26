# static function sqrt  to compute the square root of a nonnegative number c 
# given in the input using Newton's method:
# initialize t = c
# replace t with the average of c/t and t
# repeat until desired accuracy reached using condition Math.abs(t - c/t) > epsilon*t
#  where epsilon = 1e-15
import SquareRootBL as sr
try:
    number = float(input("enter a non negative number= "))

except(TypeError):
        print("the type of the input is invalid ")
sr.newtonsqrt(number)