class prime:
    def isPrime(num):
        for i in range(2,num//2+1):
            if(num%i==0):
                return False
        return True        

    def twodim():
        matrix=[]
        k=0
        for i in range(0,10):
            A=[]
            for j in range(k,k+100):
      
                if(prime.isPrime(j)):
                    
                    A.append(j)
            k+=100    
            matrix.append(A)
        p=0
        for i in matrix:
             
             string1=str(p)+'-'+ str(p+100) 
             print(string1,i)
             p+=100
                
              

prime.twodim()               


