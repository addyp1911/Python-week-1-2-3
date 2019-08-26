# a. Desc -> Take an Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) 
# where parentheses are used to order the performance of operations. 
# Ensure parentheses must appear in a balanced fashion.
# b. I/P -> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) 
# c. Logic -> Write a Stack Class to push open parenthesis “(“ and pop closed parenthesis “)”. 
# At the End of the Expression if the Stack is Empty then the Arithmetic Expression is Balanced
# Stack Class Methods are Stack(), push(), pop(), peek(), isEmpty(), size()
# d. O/P -> True or False to Show Arithmetic Expression is balanced or not.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class stack:
    def __init__(self):
        self.head=None
        self.size=0


    def append(self,data):
       
       new_node=Node(data)
       if(self.head is None):
            self.head=new_node
       t=self.head   
       while(t.next!=None):
            t=t.next
       t.next=new_node
       self.size+=1

    def pop(self,data):
        t=self.head
        if(self.head==None):
            print("the list is empty")
            return
        else:
            while(t.next!=None):
                prev=t
                t=t.next
            prev.next=None       

        size-=1              

    def printList(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next

    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False

    def size(self):
        return self.size

    def checkString(self,string1):
        stack=[]
        open_list=['(']
        close_list=[')']
        for i in string:
            if(i in open_list):
                stack.append(i)
            elif(i in close_list):
                pos=close_list.index(i)
                if(len(stack)>0 and open_list[pos]==stack[len(stack)-1]):
                    stack.pop()
                else:
                    return False    
        if(len(stack)==0):
            return True
          


#driver code
s=stack()
string="(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/3))"   
if(s.checkString(string)):
    print('the string is balanced')
else:
    print('the string is unbalanced')    

