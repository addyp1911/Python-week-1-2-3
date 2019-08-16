
class DistinctTriples:
    def findTriplets(arr,n):
        
        found = True
        for i in range (0,n-2):
            for j in range(i+1,n-1):
                    for k in range(j+1,n):
                        if(arr[i]+arr[j]+arr[k]==0):
                            print(arr[i],arr[j],arr[k])
                            found=True
        if(found==False):
            print("distinct triples not found")  
            
    arr=[-2,3,4,-2, -2, -2, 4, 4, 5,0,-1,-4]
  
    print(arr)
    findTriplets(arr,len(arr))




            
