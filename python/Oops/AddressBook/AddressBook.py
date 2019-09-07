import json
with open("/home/admin1/Desktop/address.json",'r') as f:
    my_file=json.load(f)
class AddressBook:
    def add_person(self,name,address,city,state,zipcode):
        my_dict={}
        my_dict.update({"name":name,"address":address,"city":city,"state":state,"zip":zipcode})
        my_file.append(my_dict)
    
    def update_details(self):
        data=input("enter the person details you'd like to update= ")
        for i in my_file:
            for key,value in i.items():
                if(key==data):
                    new_data=input("enter the new updated value= ")
                    i[key]=new_data

    def sort_by_zip(self):
        new_list=[]
        lst=[]
        for i in my_file:
            if(i["zip"]=="zip"):
                lst.append(i["key"]) 
        for x in sorted(lst):
            for i in my_file:
                if (i["zip"]==x):
                    new_list.append(i)
        print(new_list)            

    def sort_by_lastname(self):
        for i in my_file:
            print(type(i))
            for k,v in i.items():
                print(k)
                if(k=="name"):
                    namearr=i.get(k).split()
                    lastname=namearr[1]
                    my_file.sort(key=lastname)
        print(my_file)

a=AddressBook()        
# a.sort_by_lastname()        
a.sort_by_zip()