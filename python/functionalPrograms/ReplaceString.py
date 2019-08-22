
class ReplaceString:
    string="Hello <<username>> how are you ?"
    print(string)
    a=input("enter your name ")
    str1=string.replace("<<username>>",a)
    print(str1)