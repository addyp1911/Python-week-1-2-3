# ----------------------------------anagrams prg-----------------------------------------------
# Anagrams.py
# date : 26/08/2019
# method to check if two user entered strings are anagrams of each other 


def checkAnagrams(str1,str2):
    string1=sorted(str1)
    string2=sorted(str2)
    if(string1==string2):  #to check if all the characters in both the strings are equal to each other
        return True
    return False    