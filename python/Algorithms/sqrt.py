# static function sqrt  to compute the square root of a nonnegative number c 
# given in the input using Newton's method:
# initialize t = c
# replace t with the average of c/t and t
# repeat until desired accuracy reached using condition Math.abs(t - c/t) > epsilon*t
#  where epsilon = 1e-15
class squareroot:
    def sqrt(c):
        t=c
        epsilon=1.0e-15
        rs=epsilon*t
        i=abs(t- c//t)
        while(i>rs):
            t=(c/t + t)/2

        print(t)
#driver code
c=float(input("enter a non negative number= "))
squareroot.sqrt(c)