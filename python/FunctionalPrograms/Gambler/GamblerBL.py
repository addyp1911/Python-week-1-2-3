
# ----------------------------------Gambler prg-----------------------------------------------
# Gambler.py
# date : 26/08/2019
# method to find the number of times he/she wins and the number of bets he/she makes. 

import random
def gamble(cash,goals,nooftimes):
    i = 0
    bets = 0
    wins = 0
    while(i <= nooftimes):
        while(cash > 0 and cash <= goals):
            bets+=1

            if(random.uniform(0,1) < 0.5):
                cash += 1
            else:
                cash -= 1 

            if(cash==goals):
                wins += 1

        i += 1 


    print("the no of wins = ",wins)
    print("the percentage of wins= ",wins/nooftimes*100)                                                              
    print("the percentage of losses= ",(nooftimes-wins)/nooftimes*100)     