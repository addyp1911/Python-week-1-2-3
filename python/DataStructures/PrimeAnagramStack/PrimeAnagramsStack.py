# Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Stack using
# the Linked List and Print the Anagrams in the Reverse Order. Note no Collection
# Library can be used.

import PrimeAnagramStackBL as pa
ps= pa.PrimeAnagramStack()
for i in range(0,1001):
    for j in range(i+1,1001):
        if(ps.isprime(i) and ps.isprime(j)):
            if(ps.isanagram(i,j)):
                ps.push(i)
                ps.push(j)
ps.printlist()

