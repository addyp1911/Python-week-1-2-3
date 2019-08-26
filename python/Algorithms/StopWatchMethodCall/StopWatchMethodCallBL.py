import time
my_list=[]
strt=0
def start():
    strt=time.time()
    return strt
def stop():
    strt=start()
    duration=time.time()-strt
    return duration    

def binarysearch(arr,searchword):
    start()
    left = 0
    right = len(arr)-1
    
    while(left <= right):
            middle=left + (right-left)//2
            if(searchword == arr[middle]):
                my_list.append(stop())
                return True
            if(searchword < arr[middle]):
                right = middle-1
            else:
                left = middle+1
    
    return False


def bubblesort(arr,length):
    
    start()
    for i in range(length):
        for j in range(length-i-1):
            if(arr[j]>arr[j+1]):
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
                
    my_list.append(stop())            
        
