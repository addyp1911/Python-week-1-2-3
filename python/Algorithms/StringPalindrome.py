class StringPalindrome:
      def checkPalindrome(str):
           for i in range(0,len(str)):
                if(str[i]!=str[-(i+1)]):
                      return False

           return True
           


str=input("enter a string ")
if(StringPalindrome.checkPalindrome(str)):
       print("the string is a palindrome")
else:
   print("the string is not a palindrome")       
 
          
   
