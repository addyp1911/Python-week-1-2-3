#Merge Sort  - Write a program with Static Functions to do Merge Sort of list of Strings. 
#a. Logic -> To Merge Sort an array, we divide it into two halves, sort the two halves independently, 
#   and then merge the results to sort the full array. To sort a[lo, hi), we use the following recursive strategy:
#b. Base case: If the subarray length is 0 or 1, it is already sorted.
#c. Reduction step: Otherwise, compute mid = lo + (hi - lo) / 2, 
#   recursively sort the two subarrays a[lo, mid) and a[mid, hi), and merge them to produce a sorted result.
class MergeSort: 
 
        
    def merge( arr,l, m,r): 

     # Find sizes of two subarrays to be merged 
         n1 = m - l + 1
         n2 = r - m 
  
         L=[]
         R=[] 
  
         for i in range(0,n1):
            L[i] = arr[l + i] 
         for j in range(0,n2):
            R[j] = arr[m + 1+ j] 
  
  
  #Merge the temp arrays 
  
     #Initial indexes of first and second subarrays 
         i = 0
         j = 0
  
        # Initial index of merged subarray array 
         k = l 
         while (i < n1 and j < n2): 
      
            if (L[i] <= R[j]): 
  
                arr[k] = L[i]
                i+=1
        
            else:
         
                arr[k] = R[j]; 
                j+=1 
            
            k+=1 
         
  
        #Copy remaining elements of L[] if any 
            while (i < n1): 
      
              arr[k] = L[i] 
              i+=1 
              k+=1
     
  
        # Copy remaining elements of R[] if any 
            while (j < n2): 
      
             arr[k] = R[j]
             j+=1
             k+=1

  
    # Main function that sorts arr[l..r] using 
    # merge() 
    def sort(arr,l, r): 

        if (l < r): 
 
          # Find the middle point 
            m = (l+r)//2
  
          #Sort first and second halves 
            sort(arr, l, m) 
            sort(arr , m+1, r)
  
          # Merge the sorted halves 
            merge(arr, l, m, r)
 

        
           

  
   # Driver method 
   
arr = [12, 11, 13, 5, 6, 7] 
def printArray(arr): 
    n = len(arr); 
    for i in range(0,n):
        print(arr[i]," ")
  
print("Given Array",arr)
printArray(arr) 
  
MergeSort.sort(arr, 0, len(arr)-1) 
  
print("\nSorted array") 
printArray(arr)
