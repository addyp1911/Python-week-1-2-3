# Binary Search the Word from Word List
# a. Desc -> Read in a list of words from File. Then prompt the user to enter a word to search the list. 
# The program reports if the search word is found in the list.
# b. I/P -> read in the list words comma separated from a File and then enter the word
class BinarySearch:
   def binarySearch(arr,t):
        left=0
        right=len(arr)-1
        while(left<=right):
            middle=left+(right-left)//2
            if(arr[middle]==t):
                return True
                break
            if(t<arr[middle]):
                right=middle-1
            else:
                left=middle+1
      
 
     #driver code


#with open("/home/admin1/Desktop/sample.txt",'r') as f:

file1 = open(r"/home/admin1/Desktop/sample.txt",'r')
file_content=file1.read().split()

i=0
lst=[]
print(file_content)
for i in file_content:
    lst.append(i)
#print(lst) 
lst.sort()
#print(lst)    
str=input("enter the element you want to search in the file= ")
result=BinarySearch.binarySearch(lst,str)
if(result==True):
    print("the word is found")
else:
    print("the word is not found")        