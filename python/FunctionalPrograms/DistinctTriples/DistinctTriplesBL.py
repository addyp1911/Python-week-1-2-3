# ----------------------------------DistinctTriples prg-----------------------------------------------
# DistinctTriples.py
# date : 26/08/2019
# method to find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0



def findtriplets(arr,n):
    matrix=[]                          #empty list initialised
    for i in range (0, n-2):
        for j in range(i+1, n-1):
                for k in range(j+1,n):
                    if(arr[i]+arr[j]+arr[k] == 0):
                        new_list = []
                        new_list.append(arr[i])
                        new_list.append(arr[j])
                        new_list.append(arr[k])
                if(new_list not in matrix):    
                    matrix.append(new_list)

    for i in range(len(matrix)):
        for j in matrix[i]:
            print(j)
        print("\n")    
      
