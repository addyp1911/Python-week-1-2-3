# Hashing Function to search a Number in a slot
# Desc -> Create a Slot of 10 to store Chain of Numbers 
# that belong to each Slot to efficiently search a number from a given set of number
# I/P -> read a set of numbers from a file and take user input to search a number
# Logic -> Firstly store the numbers in the Slot. Since there are 10 Numbers divide each 
# number by 11 and the reminder put in the appropriate slot. 
# Create a Chain for each Slot to avoid Collision. 
# If a number searched is found then pop it or else push it. 
# O/P -> Save the numbers in a file

import HashingBL as hb
size=int(input("enter the size of your function= "))
hb.count(size)
for i in range(size):
    num=input("enter the number= ")
    hb.update(num,size)  
   
hb.display()