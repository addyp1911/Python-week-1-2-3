
# ----------------------------------StringPermutation prg-----------------------------------------------
#StringPermutation.py
# date : 26/08/2019
# method to print the permutations of an entered string

def permute(data, i, length): 

    if (i==length): 
        print(''.join(data) )                   #print the resultant permuted data in string format using join()

    else: 
        for j in range(i,length): 
            #swapping the characters of the string              
            data[i], data[j] = data[j], data[i] 
            permute(data, i+1, length) 
            data[i], data[j] = data[j], data[i]  