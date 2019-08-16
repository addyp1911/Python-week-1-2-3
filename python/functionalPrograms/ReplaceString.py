
class ReplaceString:
            str="Hello <<username>> how are you ?"
            print(str)
            a=input("enter your name ")
            str1=str.replace("<<username>>",a)
            print(str1)