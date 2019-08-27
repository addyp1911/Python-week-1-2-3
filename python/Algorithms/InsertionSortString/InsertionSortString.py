#insertionSort method for String
import InsertionSortString as io

arr = []                       #empty list is initialised
size = input("enter the size of the array= ")
for i in range(size):
    string = input("user please enter the element of the array= ")
    arr.append(string)

io.insertionSort(arr,size)    