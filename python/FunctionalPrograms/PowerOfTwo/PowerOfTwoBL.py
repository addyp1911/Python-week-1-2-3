
# ----------------------------------PowerOfTwo prg-----------------------------------------------
# PowerOfTwo.py
# date : 26/08/2019
# method to  print a table of the powers of 2 that are less than or equal to 2^N.

def calculate(num):
    i=0
    sum=0
    while(i<=num):
        sum+=pow(2,i)
        i=i+1 
    print(sum)


