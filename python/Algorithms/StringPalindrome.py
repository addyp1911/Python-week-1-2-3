class StringPalindrome:
      def checkPalindrome(str1):
           for i in range(0,len(str1)):
                if(str1[i]!=str1[-(i+1)]):
                      return False

           return True
           


str1=input("enter a string ")
if(StringPalindrome.checkPalindrome(str1)):
       print("the string is a palindrome")
else:
   print("the string is not a palindrome")       
 
          
   
