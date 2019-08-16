class binarySearch:
    def search(arr,t):
        left=0
        right=len(arr)-1
       
        while(left<=right):
             middle=left+(right-left)//2
             if(t==arr[middle]):
                 print("the element is found in the list")
             else:
                 print("the element is not found in the list")    
             if(t<arr[middle]):
                 right=middle-1
             else:
                 left=middle+1
        

    #driver code
    arr=[2,3,1,7,6,5]
    arr.sort()
    t=int(input("enter the element you want to search:="))
    search(arr,t)                     
