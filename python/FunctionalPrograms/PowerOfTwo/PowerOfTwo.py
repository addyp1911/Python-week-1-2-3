# 4. Power of 2 
# a. Desc -> This program takes a command-line argument N and prints a table of the powers of 2 
# that are less than or equal to 2^N.
# b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
# c. Logic -> repeat until i equals 


import PowerOfTwoBL
try:
    num=int(input("enter the highest power of 2= "))
except(ValueError):
    print("user please enter the valid power ,it should be greater than 0 and less than 31")      
PowerOfTwoBL.calculate(num) 
