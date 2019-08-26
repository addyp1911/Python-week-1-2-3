# 1. User Input and Replace String Template “Hello <<UserName>>, How are you?” 
# a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
# b. Logic -> Replace <<UserName>> with the proper name
# c. O/P -> Print the String with User Name 

import ReplaceStringBL
string = "hello username, how are you?"
# username should have minimum 3 characters
replaced_name = input("enter the name to be replaced \n")
ReplaceStringBL.replace(string, replaced_name)