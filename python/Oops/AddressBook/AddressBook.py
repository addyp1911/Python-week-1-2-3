import json
class AddressBook:
    def __init__(self):
        with open("addressbook.json",'r') as f:
            self.ab=json.load(f)    #dictionary
        print(self.ab)
        print(type(self.ab["addressbook"]))

    def add(self):
        new_dict={}
        self.name=input("enter the person's name= ")
        self.address=input("enter the address= ")
        self.city=input("enter the city= ")
        self.state=input("enter the state= ")
        self.phonenumber=input("enter the phone number= ")
        self.zipcode=input("enter the zipcode= ")
        new_dict.update({"name":self.name,"address":self.address,"city":self.city,"state":self.state,"phonenumber":self.phonenumber,"zipcode":self.zipcode})
        self.ab["addressbook"].append(new_dict)
        print(self.ab)         
        with open("addressbook.json",'w') as f:
            json.dump(self.ab,f)
            
    def update(self,upkey,index):
        for key,value in self.ab["addressbook"][index].items():
            if(key==upkey):
                val=input("enter the updated value= ")
                self.ab["addressbook"][index][key]=val      
        with open("addressbook.json",'w') as f:
            json.dump(self.ab,f) 

    def delete_person(self,name):
        my_list=[]
        for records in self.ab["addressbook"]:
                if(records["name"]!=name):
                    my_list.append(records)
        with open("addressbook.json",'w') as f:
            json.dump(my_list,f) 

    def sort_by_name(self):
        my_list=[]
        new_list=[]
        for records in self.ab["addressbook"]:
            for key,value in records.items():
                if(key=="name"):
                    last_name=records[key].split()[1]
                    my_list.append(last_name)    
        my_list.sort()
        for elem in my_list:
            for records in self.ab["addressbook"]:
                if elem in records["name"]:
                    new_list.append(records)           
        with open("addressbook.json",'w') as f:
            json.dump(new_list,f) 
    
    def sort_by_zip(self):
        my_list=[]
        new_list=[]
        for records in self.ab["addressbook"]:
            for key,value in records.items():
                if(key=="zipcode"):
                    my_list.append(records[key])    
        my_list.sort()
        for elem in my_list:
            for records in self.ab["addressbook"]:
                if elem in records["zipcode"]:
                    new_list.append(records)           
        with open("addressbook.json",'w') as f:
            json.dump(new_list,f) 


if __name__ == "__main__":
        
    a=AddressBook()
    while(True):
        i=int(input("1.enter 1 to add a new person to addressbook\n2.enter 2 to delete a person\n3.enter 3 to sort the addressbook by lastname\n4.enter 4 to update the addressbook\n5. enter 5 to exit the application\n6.enter 6 to sort the addressbook by zipcode\n"))     
        if i ==1:
            a.add()
        elif i==4:
            index=int(input("enter the index of the addressbook you would update= "))
            key=input("enter the detail you'd like to update= ")
            if(key=="name"):
                print("cannot update name!")
            else:
                a.update(key,index)
        elif i==2:
            name=input("enter the name pf the person whose record you would delete= ")
            a.delete_person(name)
        elif i==3:
            a.sort_by_name()    
        elif i==5:
            exit()
            break
        elif i==6:
            a.sort_by_zip()
            continue
