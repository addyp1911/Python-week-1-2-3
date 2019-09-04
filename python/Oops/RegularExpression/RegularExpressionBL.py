# ----------------------------------RegularExpression prg-----------------------------------------------
# RegularExpression.py
# date : 27/08/2019
# method to use Regex to replace name, full name, Mobile#, and Date with proper value.

import re
def change_expression(string):
    for i in string:
#check for a match with the <<name>> as written in the json file using regex format         
        if(re.match("<<\\bname\\b>>",i)):
            name=input("enter the name: ")
                                      #replacing the <<name>> with the user entered first name            
            string[string.index(i)]=name
#check for a match with the <<fullname>> as written in the json file using regex format      
        if(re.match("<<\\bfullname\\b>>",i)): 
            full_name=input("enter the full name: ")
            if(len(full_name) < 8):
#if the length of the fullname is less than 8,then asking user to enter it properly
                print("please user enter your full name!")
                input("your fullname= ")
                                     #replacing the <<fullname>> with the user entered first name  
            string[string.index(i)]=full_name

#check for a match with 91-­xxxxxxxxxx as written in the json file using regex format 
        if(re.match("\\b91-\w+.\\b",i)):
            phone_num=int(input("enter the phone number= "))

            if(len(str(phone_num))<10):   #if the length of the fullname is less than 10,then asking user to enter it properly
                print("invalid phone number!")  
            else:
                string[string.index(i)] =phone_num 
#check for a match with 01/01/2016. as written in the json file using regex format                           
        if(re.match(r"^\w{2}\/\w{2}\/\w{4}.$",i)):

            current_date=input("enter the current date= ")
            if(current_date.isdigit()!=True):  #if the date has alphabets,then asking user to enter it properly
                print("the date entered is invalid! ")
                current_date=input("please enter the valid date= ")
            string[string.index(i)]=current_date


    print("the modified user entered string is as follows ",string)