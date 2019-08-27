import PalindromeBL as pb
p=pb.Palindrome()
i=0
for i in range(10,1000):
    if(p.isprime(i)):
        if(p.checkpalindrome(i)):
            print(i)
    

