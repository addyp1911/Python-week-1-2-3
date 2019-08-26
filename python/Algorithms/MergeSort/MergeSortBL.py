# ----------------------------------mergesort prg-----------------------------------------------
# mergesort.py
# date : 26/08/2019
# method to sort a user entered array using merge sort

def merge(arr,left,middle,right):    #to merge the sorted left and right halves
    n1 = middle-left+1
    n2 = right-middle

    L = []    #initialising empty lists
    R = []
    
    for i in range(0,n1):
        L[i] = arr[i+left]
    for j in range(0,n2):
        R[j] = arr[j+middle+1] 
    
    i = 0
    j = 0
    k = left
    while(i<n1 and j<n2):
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1   

    while(i < n1):
        arr[k] = L[i]
        i +=1
        k +=1

    while(j<n2):
        arr[k] = R[j]
        j +=1
        k +=1

def sortarray(arr,left,right):          #to sort the array by dividing each array from the  middle index
 
    if(left < right):
        middle =(left+right)//2
        sortarray(arr,left,middle)
         
        sortarray(arr,middle+1,right)
        merge(arr,left,middle,right)