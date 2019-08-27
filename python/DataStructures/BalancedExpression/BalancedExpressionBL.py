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

    def isempty(self):
        if(self.size==0):
            return True
        else:
            return False

    def size(self):
        return self.size

    def checkstring(self,string1):
        stack=[]
        open_list=['(']
        close_list=[')']
        for i in string1:
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