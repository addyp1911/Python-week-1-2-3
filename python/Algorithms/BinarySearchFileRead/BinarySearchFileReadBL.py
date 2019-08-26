#with open("/home/admin1/Desktop/sample.txt",'r') as f:
def disp(arr,t):
    left=0
    right=len(arr)-1
    while(left<=right):
        middle=left+(right-left)//2
        if(arr[middle]==t):
            return True
            break
        if(t<arr[middle]):
            right=middle-1
        else:
            left=middle+1
    
   