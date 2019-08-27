# binarySearch method for string array

import BinarySearchBL as bs
arr=[]                           #empty list initialised
size=int(input("enter the size of the array= "))
for i in range(0,size):
    try:

        a=input("enter the element= ")               #Enter any string to search for in the user entered array
        arr.append(a)


arr.sort()
searchele = input("enter the element you want to search= ")
res=bs.search(arr,searchele) 

if(res):
    print("the element is found in the list")
else:
    print("the element is not found in the list") 
                    
