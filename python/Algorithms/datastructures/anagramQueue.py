class Node:
    def __init__(self, data):
          self.data = data
          self.head=None
class queue:
    def __init__(self):
          self.head=None
              

    def enqueue(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node 
            return
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node

    def dequeue(self):
        if(self.head is None):
            print("the list is empty")
            return

        obj=self.head.data
        self.head=self.head.next
        return obj

    def isAnagram(self,num1,num2):
        n1=str(num1)
        n2=str(num2)
        sorted(n1)
        sorted(n2)
        return n1==n2

    def isPrime(self,num):
        for i in range(2,num//2):
            if(num%i==0):
                return False
        return True

    def add(self):
        for i in range(1,50):
            for j in range(i+1,50):
                if(q.isPrime(i) and q.isPrime(j)):
                    if(q.isAnagram(i,j)):
                        q.enqueue(i)
                        q.enqueue(j)
    def printList(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next

                        

q=queue()
q.add()

