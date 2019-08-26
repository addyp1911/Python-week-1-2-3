
# ----------------------------------squareroot prg-----------------------------------------------
# SquareRoot.py
# date : 26/08/2019
# method to find the squareroot of a non negative number using newton's method


def newtonsqrt(number):
    temp=number
    epsilon=1e-15
    while(abs(temp- (number/temp))>epsilon*temp):
        temp=(number/temp + temp)/2.0
    print(temp)
