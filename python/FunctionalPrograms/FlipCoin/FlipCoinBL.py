import random
def check(noOfTimes): 
    heads = 0
    tails = 0
    for i in range(1, noOfTimes+1):
        coin=random.uniform(0,1)
        if(coin < 0.5):
            heads += 1
        else:
            tails += 1
    print("the percentage of heads out of total times coin is flipped",heads/noOfTimes*100)        
    print("the percentage of tails out of total times coin is flipped",(noOfTimes-heads)/noOfTimes*100)              