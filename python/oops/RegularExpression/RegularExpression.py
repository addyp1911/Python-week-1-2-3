# Read in the following message: Hello <<name>>, We have your full
# name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx.
# Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
# Use Regex to replace name, full name, Mobile#, and Date with proper value.

import re
with open("/home/admin1/Desktop/regex.txt",'r') as f:
    string=f.read().split()
    print(string)
for i in string:
    if(re.match("<<\\bname\\b>>",i)):
        name=input("enter the name: ")
        string[string.index(i)]=name
    if(re.match("<<\\bfullname\\b>>",i)):
        full_name=input("enter the full name: ")
        if(len(full_name)<10):
            print("please user enter your full name!")
            input("your fullname= ")
        string[string.index(i)]=full_name
    if(re.match("\\b91-\w+.\\b",i)):
        phone_num=int(input("enter the phone number= "))
        if(len(str(phone_num))<10):
            print("invalid phone number!")
        else:
            string[string.index(i)] =phone_num          
    if(re.match("^\w{2}\/\w{2}\/\w{4}.$",i)):
        current_date=input("enter the current date= ")
        string[string.index(i)]=current_date
    print(string)
