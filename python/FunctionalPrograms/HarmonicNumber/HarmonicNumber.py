# 5. Harmonic Number 
# a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N 
# b. I/P -> The Harmonic Value N. Ensure N != 0
# c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
# d. O/P -> Print the Nth Harmonic Value.



import HarmonicNumberBL
try:
    num=int(input("Enter the value for the nth harmonic number= ")) 
except(TypeError,ValueError):
    print("user please enter a positive integer value greater than or equal to 1")

HarmonicNumberBL.countharmonic(num)