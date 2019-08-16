#    1. An Anagram Detection Example
#a. Desc -> One string is an anagram of another if the second is simply a rearrangement of the first. For example, 'heart' and 'earth' are anagrams...
#b. I/P -> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
#c. O/P -> The Two Strings are Anagram or not....
from collections import Counter
class Anagrams:
    def checkAnagrams(str1,str2):
       return Counter(str1) == Counter(str2) 
       
a=input("enter the first string ")
b=input("enter the second string ")
rs=Anagrams.checkAnagrams(a,b)
if(rs):
    print("the strings are anagrams")
else:
    print("the strings are not anagrams")