# I/P -> Write main function to call the utility function
# Logic -> Check using Stopwatch the Elapsed Time for every method call
# O/P -> Output the Search and Sorted List. More importantly print elapsed time
# performance in descending order


import StopWatchMethodCallBL as sw
arr=[]
num =int(input("enter the size= "))            
for i in range(num):
    n=int(input("enter the element= "))
    arr.append(n)
    arr_copy=arr.copy()

time1=sw.bubblesort(arr,len(arr))
print("the sorted array is =",arr)

search_num=int(input("enter the number to search for in the array= "))
time2=sw.binarysearch(arr_copy,search_num)
sw.my_list.sort(reverse=True)
print(sw.my_list)
