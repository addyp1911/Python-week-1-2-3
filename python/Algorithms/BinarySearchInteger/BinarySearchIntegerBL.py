def search(arr,t):
    left=0
    right=len(arr)-1
    
    while(left<=right):
            middle=left+(right-left)//2
            if(t==arr[middle]):
                return True
            if(t<arr[middle]):
                right=middle-1
            else:
                left=middle+1
    
