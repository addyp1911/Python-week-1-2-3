# ----------------------------------replace prg-----------------------------------------------
# ReplaceString.py
# date : 22/08/2019
# method to replace the name


def replace(statement, replaced_name):
    if len(replaced_name) >= 3:
        print(statement.replace("username", replaced_name))
    else:
        print("enter the valid name to be replaced")
     