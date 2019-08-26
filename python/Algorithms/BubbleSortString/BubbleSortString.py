# bubbleSort method for String
import BubbleSortStringBL as bs

arr = []                       #empty list is initialised
size = int(input("enter the size of the array= "))
for i in range(size):
    string = input("user please enter the element of the array= ")
    arr.append(string)

 
bs.bubblesort(arr,size)      