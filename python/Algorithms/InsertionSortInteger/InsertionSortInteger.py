#insertionSort method for integer
import InsertionSortIntegerBL as i

arr = []                                     #empty list is initialised
                     
size = int(input("enter the size of the array= "))
for i in range(size):
    num = int(input("user please enter the element of the array= "))
    arr.append(num)

i.insertionsort(arr,len(arr))           