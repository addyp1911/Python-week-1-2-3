
import random
class Gambler:
    
        cash= int(input("enter the stake with the gambler ")) 
        goals=int(input("enter the goal he has to achieve "))
        noOfTimes=int(input("the number of times he plays "))
        i=0
        bets=0
        wins=0
        while(i<=noOfTimes):
            bets+=1
            while(cash>0 & cash<=goals):
                if(random.random()<0.5):
                    cash+=1
                else:
                    cash-=1 
            if(cash==goals):
                 wins+=1

            i+=1                                          
        print("the no of wins = ",wins)
        print("the percentage of wins= ",wins/noOfTimes*100)                                                              
        print("the percentage of losses= ",noOfTimes-wins/noOfTimes*100) 
