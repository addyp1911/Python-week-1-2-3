class Node:
    def __init__(self, data):
        self.data=data
        self.next=next

class PrimeAnagramStack:
    def __init__(self):
          self.head =None
          self.size=0

    def push(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node
        self.size+=1

    def pop(self):
        if(self.head is None):
            print("the stack is empty")
            return
        obj=self.head.data
        self.head=self.head.next
        self.size-=1
        return obj


    def size(self):
        return self.size        

    def peek(self):
        return self.head.data

    def printlist(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next    


    def isanagram(self,num1,num2):
        n1=str(num1)
        n2=str(num2)
        x=sorted(n1)
        y=sorted(n2)

        return x==y

    def isprime(self,num):
        for i in range(2,num//2+1):
            if(num%i==0):
                return False
        return True

