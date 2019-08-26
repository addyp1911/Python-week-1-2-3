# ----------------------------------binarysearchfileread prg-----------------------------------------------
# BinarySearchFileRead.py
# date : 26/08/2019
# method to search for a user entered word from a list of words read from a file using binary search algorithm

def display(arr,search_element):
    left=0
    right=len(arr)-1
    while(left<=right):
        middle=left+(right-left)//2              #finding the middle index of the array to search for the user entered element
        if(arr[middle]==search_element):         #if found,the method returns true
            return True
            
        if(search_element<arr[middle]):
            right=middle-1
        else:
            left=middle+1
    
   