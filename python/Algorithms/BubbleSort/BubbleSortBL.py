# ----------------------------------bubblesort prg-----------------------------------------------
# BubbleSort.py
# date : 26/08/2019
# method to sort a user entered array of integers using bubble sort algorithm
def bubblesort(arr,size):
    for i in range(0,size):
        for j in range(0,size-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    for i in range (0,size):
        print(arr[i],",")             