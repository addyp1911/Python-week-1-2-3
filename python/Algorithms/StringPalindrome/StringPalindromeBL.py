
def checkpalindrome(str1):
    for i in range(0,len(str1)):
        if(str1[i]!=str1[-(i+1)]):
                return False

    return True