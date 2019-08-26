
# ----------------------------------HarmonicNumber prg-----------------------------------------------
# HarmonicNumber.py
# date : 26/08/2019
# method to print the Nth harmonic number


def countharmonic(num):
    count = 1
    sum = 0.0
    while(count <= num):
        sum =sum + float(1/count)
        count += 1
    print(sum)               