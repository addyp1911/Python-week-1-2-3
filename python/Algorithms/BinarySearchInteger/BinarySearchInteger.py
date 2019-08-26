import BinarySearchIntegerBL as bs
arr=[]
num=int(input("enter the size of the array= "))
for i in range(0,num+1):
    a=int(input("enter the element= "))
    arr.append(a)
arr.sort()
t=int(input("enter the element you want to search:="))
res=bs.search(arr,t) 
if(res):
    print("the element is found in the list")
else:
    print("the element is not found in the list") 


