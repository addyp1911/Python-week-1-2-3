class Palindrome:
    
    def checkpalindrome(n):
        t=n
        rev=0
        while(n!=0):
            rev=rev*10+n%10
            n//=10
        if(rev==t):
          return True

    def isprime(n):
        
        for i in range(2,(n//2+1)):
            if(n%i==0):
               return False
               
        return True
            
