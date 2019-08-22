# Hashing Function to search a Number in a slot
# Desc -> Create a Slot of 10 to store Chain of Numbers 
# that belong to each Slot to efficiently search a number from a given set of number
# I/P -> read a set of numbers from a file and take user input to search a number
# Logic -> Firstly store the numbers in the Slot. Since there are 10 Numbers divide each 
# number by 11 and the reminder put in the appropriate slot. 
# Create a Chain for each Slot to avoid Collision. 
# If a number searched is found then pop it or else push it. 
# O/P -> Save the numbers in a file
slot=[]
a=[]

def count(size):
    for i in range(size):
        slot.append(str(i))
    for j in range(size):
        slot.append([])
    print(slot)

def update(value,size):
    slot[int(value)%size+1].append(value)

def display():
    for i in slot[0]:
        print(i,slot[i+1])

size=int(input("enter the size of your function= "))
count(size)
for i in range(size):
    num=input("enter the number= ")
    update(num,size)  
   
display()