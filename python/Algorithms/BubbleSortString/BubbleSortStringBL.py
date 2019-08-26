# ----------------------------------bubblesort prg-----------------------------------------------
# BubbleSort.py
# date : 26/08/2019
# method to sort a user entered array of strings using bubble sort algorithm
def bubbleSort(arr,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t


    for i in range(0,n):
        print(arr[i])           
