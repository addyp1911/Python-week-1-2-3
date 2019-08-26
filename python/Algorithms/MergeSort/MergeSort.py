#Merge Sort  - Write a program with Static Functions to do Merge Sort of list of Strings. 
#a. Logic -> To Merge Sort an array, we divide it into two halves, sort the two halves independently, 
#   and then merge the results to sort the full array. To sort a[lo, hi), we use the following recursive strategy:
#b. Base case: If the subarray length is 0 or 1, it is already sorted.
#c. Reduction step: Otherwise, compute mid = lo + (hi - lo) / 2, 
#   recursively sort the two subarrays a[lo, mid) and a[mid, hi), and merge them to produce a sorted result.

import MergeSortBL 

arr=[]
size = int(input("enter the size of the array to be sorted= "))

for i in range(size):
    num = int(input("enter the element of the array= "))
    arr.append(num)

print("the unsorted array is= ",arr)

right=len(arr)-1
MergeSortBL.srt(arr,0,right)
print("the sorted array is= ",arr)    

