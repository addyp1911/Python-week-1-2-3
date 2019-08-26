# ----------------------------------binarysearchstring prg-----------------------------------------------
# BinarySearchString.py
# date : 26/08/2019
# method to search for a user entered word from an array of strings using binary search algorithm

def search(arr,searchword):
    left = 0
    right = len(arr)-1
    
    while(left <= right):
            middle=left + (right-left)//2
            if(searchword == arr[middle]):
                return True
            if(searchword < arr[middle]):
                right = middle-1
            else:
                left = middle+1
    
    return  stop()