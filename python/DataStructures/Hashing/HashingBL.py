# ----------------------------------Hashing prg-----------------------------------------------
# Hashing.py
# date : 26/08/2019
# method to implement the hashing algorithm

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