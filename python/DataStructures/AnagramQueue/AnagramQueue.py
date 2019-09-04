# Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Queue using
# the Linked List and Print the Anagrams from the Queue. Note no Collection Library
# can be used.

import AnagramQueueBL as aq
q=aq.Queue() 
for i in range(0,1001):
    for j in range(i+1,1001):
        if(q.isprime(i) and q.isprime(j)):
            if(q.isanagram(i,j)):
                q.enqueue(i)
                q.enqueue(j)

q.printlist()