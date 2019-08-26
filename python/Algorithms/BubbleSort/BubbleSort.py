# Bubble Sort
# a. Desc -> Reads in integers prints them in sorted order using Bubble Sort
# b. I/P -> read in the list ints
# c. O/P -> Print the Sorted List

import BubbleSortBL as bs

arr = []                     #empty list is initialised
size = int(input("enter the size of the array= "))
for i in range(size):
    num = int(input("user please enter the element of the array= "))
    arr.append(num)

           
bs.bubbleSort(arr,size)