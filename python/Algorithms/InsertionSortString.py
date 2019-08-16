#insertionSort method for String
class InsertionSortString:
    def insertionSort(arr,n):
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while(j>=0 and arr[j]> key):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key    
        for i in range(0,n):
            print(arr[i])

            #driver code
    arr=["I","LOVE","PYTHON","AS","MY","TECHNOLOGY"]
    insertionSort(arr,len(arr))    