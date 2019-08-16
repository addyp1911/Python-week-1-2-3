#insertionSort method for integer
class InsertionSort:
    def insertionSort(arr,n):
        j=0
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while(j>=0 and arr[j]>key):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key    
        for i in range(0,n):
            print(arr[i]) 
    arr=[23,12,1,34,0,43,5] 
    insertionSort(arr,len(arr))           