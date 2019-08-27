# ----------------------------------swapnibble prg-----------------------------------------------
# SwapNibble.py
# date : 26/08/2019
# method to swap the nibbles of a decimal number after binary conversion

class SwapNibble:

    def bintodec(self,bin):
            dec = 0
            c = 0
            while(bin != 0):
                r=bin % 10
                dec+=r * pow(2,c)
                bin1 //= 10
                c += 1
            return dec 
        
    def dectobin(self,dec):
        bin1 = ""
        while(dec != 0):
            r=dec % 2
            bin1=str(r) + bin1
            dec //= 2
        return bin1

    def swapnibbles(self,bin1):
        l=len(bin1)
        if(l <8):
            while(l != 8):
                bin1="0" + bin1
                l += 1
        swap=bin1[4:]+bin1[0:4] 
        return swap
