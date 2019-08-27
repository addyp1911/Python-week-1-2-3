# 10. Sum of three Integer adds to ZERO
# a. Desc -> A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
# b. I/P -> N number of integer, and N integer input array
# c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
# d. O/P -> One O                                                                                                                                                                                                                                                                                                                                                          utput is number of distinct triplets 
# as well as the second output is to print the distinct triplets.

    
import DistinctTriplesBL     
try:
    arr=[]     
    size=int(input("enter the size of the array= "))
    
    for i in range(size):
        num=int(input("enter the elements to be added to the array= "))
        arr.append(num)
except:
    print("enter the valid integer input for the data")

new_arr=sorted(arr)
DistinctTriplesBL.findtriplets(new_arr,size)




            
