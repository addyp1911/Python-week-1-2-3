# 16. Write Binary.java to read an integer as an Input, convert to Binary using toBinary function
# i. Swap nibbles and find the new number.
# ii. Find the resultant number is the number is a power of 2.

import SwapNibbleBL as sb
obj=sb.SwapNibble()
a=int(input("enter a decimal number "))
bin1=obj.decTobin1(a)

print(bin1) 
swap=obj.swapNibbles(bin1)
print("after swapping the nibbles we get")
print(swap)
print("decimal equivalent of the swapped bin1ary number")
dv=obj.bin1ToDec(int(swap))
print(dv)
