#Merge Sort  - Write a program with Static Functions to do Merge Sort of list of Strings. 
#a. Logic -> To Merge Sort an array, we divide it into two halves, sort the two halves independently, 
#   and then merge the results to sort the full array. To sort a[lo, hi), we use the following recursive strategy:
#b. Base case: If the subarray length is 0 or 1, it is already sorted.
#c. Reduction step: Otherwise, compute mid = lo + (hi - lo) / 2, 
#   recursively sort the two subarrays a[lo, mid) and a[mid, hi), and merge them to produce a sorted result.
def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        L[i].append(arr[i])
    for j in range(0,n2):
        R[j].append(arr[j]) 
    
    i=0
    j=0
    k=l
    while(i<n1 and j<n2):
        if(L[i]<=R[j]):
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1   

    while(i<n1):
        arr[k]=L[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=R[j]
        j+=1
        k+=1

         
def sort(arr,l,r):
    if(l<r):
        m=l+r//2
        sort(arr,m,l)
        sort(arr,m+1,r)
        merge(arr,l,m,r)
    return arr

#driver code
arr=[8,9,3,2,4,5] 
print("the unsorted array is= ",arr)
res=sort(arr,0,len(arr))
print("the sorted array is= ",res)    

