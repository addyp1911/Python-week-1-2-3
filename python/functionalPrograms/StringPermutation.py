class StringPermutation:
  def permutation(string):
        lst=list(string)
        results=[]
        results.append(""+lst[0])
        for i in range(1,len(lst)):
            c=lst[i]
            size = len(results)
        j=size-1
        while(j>=0): 
         string1 = results.pop(j)
         for l in range(0,len(string1)+1):
            results.append(string1[0:l] + c + string1[l])
         j-=1
        #print("Number of Permutations: " + str(len(results)))
        print(results)
#Driver code
st=input("enter the string to be permutated= ")
StringPermutation.permutation(st)        

