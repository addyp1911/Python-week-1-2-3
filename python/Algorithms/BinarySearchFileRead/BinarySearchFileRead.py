# Binary Search the Word from Word List
# a. Desc -> Read in a list of words from File. Then prompt the user to enter a word to search the list. 
# The program reports if the search word is found in the list.
# b. I/P -> read in the list words comma separated from a File and then enter the word
import BinarySearchFileReadBL as bs

file1 = open("/home/admin1/Desktop/sample.txt",'r')
file_content=file1.read().split()
file_content.sort()    
string=input("enter the element you want to search in the file= ")
result=bs.disp(file_content,string)
if(result==True):
    print("the word is found")
else:
    print("the word is not found")        
      
