# 5. Harmonic Number 
# a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N 
# b. I/P -> The Harmonic Value N. Ensure N != 0
# c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
# d. O/P -> Print the Nth Harmonic Value.



import HarmonicNumberBL
a=input("Enter the value") 
num=int(a)
HarmonicNumberBL.countHarmonic(num)