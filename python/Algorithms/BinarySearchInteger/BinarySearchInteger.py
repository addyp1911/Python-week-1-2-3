#Binarysearch algorithm to search for a user entered integer from an array of integers

import BinarySearchIntegerBL as bs

arr=[]                                             #empty list is initialised

size=int(input("enter the size of the array= "))

for i in range(0,size):

    a=int(input("enter the element= "))               #type casting the element to be searched into int type
    arr.append(a)

arr.sort()

searchnumber=int(input("enter the element you want to search= "))
result=bs.search(arr,searchnumber) 
if(result):
    print("the element is found in the list")
else:
    print("the element is not found in the list") 


