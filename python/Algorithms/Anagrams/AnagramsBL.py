def checkAnagrams(str1,str2):
    string1=sorted(str1)
    string2=sorted(str2)
    if(string1==string2):
        return True
    return False    