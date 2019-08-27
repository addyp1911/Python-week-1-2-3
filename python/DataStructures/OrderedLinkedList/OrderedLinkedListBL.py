class Node:
    def __init__(self,data):
          self.data = data
          self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def addfirst(self,data):
        new_node=Node(data)
        if(self.head is None):
            new_node.next=self.head
            self.head=new_node

        new_node.next=self.head

    def addlast(self,data):
        new_node=Node(data)
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node

    def sort(self,list1):
       
        i=j=temp=0
        n=len(list1)

        for i in range(0,n):
            for j in range(0,n-i-1):
                if(list1[j]>list1[j+1]):
                    temp=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=temp
        return list1            

        
    def printlist(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next