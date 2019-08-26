def findTriplets(arr,n):
    matrix=[]
    found = True
    for i in range (0, n-2):
        for j in range(i+1, n-1):
                for k in range(j+1,n):
                    if(arr[i]+arr[j]+arr[k] == 0):
                        list1 = []
                        list1.append(arr[i])
                        list1.append(arr[j])
                        list1.append(arr[k])
                        if(list1 not in matrix):    
                            matrix.append(list1)
    print(matrix)
      
