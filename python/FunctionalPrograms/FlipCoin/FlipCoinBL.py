# ----------------------------------FlipCoin prg-----------------------------------------------
#FlipCoin.py
# date : 26/08/2019
# method to measure the percentage of Head vs Tails using random function to get value between 0 and 1.


import random

def check(nooftimes): 
    heads = 0
    tails = 0
    for i in range(1, nooftimes+1):
        coin=random.random()
        if(coin < 0.5):
            heads += 1
        else:
            tails += 1

    print("the percentage of heads out of total times coin is flipped",heads/nooftimes*100)        
    print("the percentage of tails out of total times coin is flipped",(nooftimes-heads)/nooftimes*100)              