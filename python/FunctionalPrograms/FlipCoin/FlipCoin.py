# 2. Flip Coin and print percentage of Heads and Tails
# a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
# b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
# c. O/P -> Percentage of Head vs Tails

import FlipCoinBL
try:
    nooftimes = int(input("enter the no of times the coin is flipped= "))
except:
    print("enter the valid positive integer input for the number of times a coin is flipped") 

FlipCoinBL.check(nooftimes)            