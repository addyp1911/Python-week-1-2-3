# Desc -> Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke 
# (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the number 
# of bets he/she makes. 
# Run the experiment N times, averages the results, and prints them out.
import GamblerBL
cash= int(input("enter the stake with the gambler ")) 
goals=int(input("enter the goal he has to achieve "))
noOfTimes=int(input("the number of times he plays ")) 
GamblerBL.gamble(cash,goals,noOfTimes)                                     

