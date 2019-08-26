
# Write static functions to return all permutation of a String using iterative method and Recursion method. 
# Check if the arrays returned by two string functions are equal.

import StringPermutationBL

string = input("enter the string you want to permute= ")
size = len(string) 
data = list(string)               #type casting the entered string into list type to permute it character by character
StringPermutationBL.permute(data, 0, size)