# a. Desc -> Take an Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) 
# where parentheses are used to order the performance of operations. 
# Ensure parentheses must appear in a balanced fashion.
# b. I/P -> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) 
# c. Logic -> Write a Stack Class to push open parenthesis “(“ and pop closed parenthesis “)”. 
# At the End of the Expression if the Stack is Empty then the Arithmetic Expression is Balanced
# Stack Class Methods are Stack(), push(), pop(), peek(), isEmpty(), size()
# d. O/P -> True or False to Show Arithmetic Expression is balanced or not.


import BalancedExpressionBL as be          

s=be.stack()
try:
    string=input("enter the string to check if it's balanced or not= ")
except:
    print("enter a valid expression with parantheses")
if(s.checkString(string)):
    print('the string is balanced')
else:
    print('the string is unbalanced')    

