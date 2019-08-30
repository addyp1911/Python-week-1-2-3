# Read in the following message: Hello <<name>>, We have your full
# name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx.
# Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
# Use Regex to replace name, full name, Mobile#, and Date with proper value.

import RegularExpressionBL as rg
with open("/home/admin1/Desktop/regex.txt",'r') as f:
    string=f.read().split()   #reading the entered text from the text file,storing word by word in a list
    print(string)
    rg.change_expression(string)

