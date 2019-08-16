class SwapNibbles:
    def bin1ToDec(bin1):
        dec=0
        c=0
        while(bin1!=0):
            r=bin1%10
            dec+=r*pow(2,c)
            bin1//=10
            c+=1
        return dec 
       
    def decTobin1(dec):
        bin1=""
        while(dec!=0):
            r=dec%2
            bin1=str(r)+bin1
            dec//=2
        return bin1

    def swapNibbles(bin1):
        l=len(bin1)
        if(l<8):
          while(l!=8):
            bin1="0"+bin1
            l+=1
        swap=bin1[4:]+bin1[0:4] 
        return swap


    #Driver code

    a=int(input("enter a decimal number "))
    bin1=decTobin1(a)
    
    print(bin1) 
    swap=swapNibbles(bin1)
    print("after swapping the nibbles we get")
    print(swap)
    print("decimal equivalent of the swapped bin1ary number")
    dv=bin1ToDec(int(swap))
    print(dv)
