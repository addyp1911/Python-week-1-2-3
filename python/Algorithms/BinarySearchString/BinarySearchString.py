# binarySearch method for String
import BinarySearchBL as bs

arr=["hi","i","love","programming","in","python"]
arr.sort()
t=input("enter the element you want to search:=")
res=bs.search(arr,t) 
if(res):
    print("the element is found in the list")
else:
    print("the element is not found in the list") 
                    
