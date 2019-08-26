
# Write static functions to return all permutation of a String using iterative method and Recursion method. 
# Check if the arrays returned by two string functions are equal.

import StringPermutationBL
string = input("enter the string you want to permute= ")
n = len(string) 
data = list(string) 
StringPermutationBL.permute(data, 0, n)