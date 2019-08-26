# 10. Sum of three Integer adds to ZERO
# a. Desc -> A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
# b. I/P -> N number of integer, and N integer input array
# c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
# d. O/P -> One O                                                                                                                                                                                                                                                                                                                                                          utput is number of distinct triplets 
# as well as the second output is to print the distinct triplets.

    
import DistinctTriplesBL           
arr=[-2,3,4,-2,5,0,-1,-4,3,4,4,4,4]
arr1=sorted(arr)
DistinctTriplesBL.findTriplets(arr1,len(arr))




            
