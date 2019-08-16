

class Harmonic:
               a=input("Enter the harmonic value") 
               num=int(a)
               count=1
               sum=0.0
               while(count<=num):
                                 sum= sum+float(1/count)
                                 count+=1
               print(sum)               