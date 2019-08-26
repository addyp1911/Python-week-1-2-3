# 16. Write Binary.java to read an integer as an Input, convert to Binary using toBinary function
# i. Swap nibbles and find the new number.
# ii. Find the resultant number is the number is a power of 2.

import SwapNibbleBL as sb

obj=sb.SwapNibble()
a=int(input("enter a decimal number= "))

binary1=obj.dectobin(a)
#the binary equivalent of the decimal number is returned
print(binary1)

swap=obj.swapnibbles(binary1)        #the nibbles of the binary equivalent is swapped
print("after swapping the nibbles we get= ")
print(swap)
print("decimal equivalent of the swapped binary number is = ")  
 # the final decimal result after nibble swap is obtained as follows
result=obj.bintodec(int(swap))
print(result)
