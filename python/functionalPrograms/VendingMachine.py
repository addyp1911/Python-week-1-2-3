# Find the Fewest Notes to be returned for Vending Machine                                                                                                                                                                                                                                                                                                                                                                                                                 
# Desc -> There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes
# which can be returned by Vending Machine. 
# Write a Program to calculate the minimum number of Notes as well as the Notes to be returned by the Vending Machine as a Change
# I/P -> read the Change in Rs to be returned by the Vending Machine
# Logic -> Use Recursion and check for largest value of the Note to 
# return change to get to minimum number of Notes. 
# O/P -> Two Outputs -one the number of minimum Note needed to give the change 
# and second list of Rs Notes that would given in the Change

class VendingMachine:
    def calculateChange(bill):
        notes=[1000,500,100,50,20,10,5,2,1]
        notes_counter=[]
        for i in range(0,9):
            if(bill>=notes[i]):
                notes_counter.append(bill//notes[i])
                bill=bill-notes[i]*notes_counter[i]
            else:
                notes_counter.append(0)    


        for i in range(0,9):
            if(notes_counter[i]!=0):
                print(notes[i], notes_counter[i] ) 

#driver code
amount=int(input("print the bill of the product bought= "))
VendingMachine.calculateChange(amount)




