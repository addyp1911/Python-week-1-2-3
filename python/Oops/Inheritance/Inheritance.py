class Parent:          #parent class
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
    
    def details(self):
        school=input("enter the school name of the student= ")
        return school


class Child(Parent):        #child class inheriting the parent class amnd calling the parent class constructor
    def __init__(self,name,age):
        # Parent. __init__(self,name,age)
        super().__init__(name,age)
    last_name=input("enter the lastname of the person= ")
          
#driver code
c=Child("harsha",10)
print(c.last_name)      #using the child class object to access the child class states and variables   
print(c.details())          