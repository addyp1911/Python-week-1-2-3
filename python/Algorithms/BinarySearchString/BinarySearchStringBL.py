# ----------------------------------binarysearchfileread prg-----------------------------------------------
# BinarySearchInteger.py
# date : 26/08/2019
# method to search for a user entered word from an array of integers using binary search algorithm

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
    

    

