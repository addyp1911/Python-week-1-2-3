# ----------------------------------insertionsort prg-----------------------------------------------
# InsertionSort.py
# date : 26/08/2019
# method to sort a user entered array of strings using insertion sort algorithm
def insertionSort(arr,size):
        for i in range(1,size):
            key=arr[i]
            j=i-1
            while(j>=0 and arr[j]> key):
                arr[j+1] = arr[j]
                j-=1

            arr[j+1] = key  

        for i in range(0,size):
            print(arr[i])