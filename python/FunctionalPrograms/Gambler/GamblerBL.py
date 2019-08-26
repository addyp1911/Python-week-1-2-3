import random
def gamble(cash,goals,noOfTimes):
    i = 0
    bets = 0
    wins = 0
    while(i<=noOfTimes):
        while(cash > 0 and cash <= goals):
            bets+=1
            if(random.uniform(0,1)<0.5):
                cash += 1
            else:
                cash -= 1 
        if(cash==goals):
                wins += 1

        i += 1 
    print("the no of wins = ",wins)
    print("the percentage of wins= ",wins/noOfTimes*100)                                                              
    print("the percentage of losses= ",(noOfTimes-wins)/noOfTimes*100)     