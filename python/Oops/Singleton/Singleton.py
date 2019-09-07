class Singleton(object):
    instance=None

    @classmethod
    def instance_(cls):               #class method
        if(cls.instance==None):
            cls.instance=Singleton()
        return cls.instance

    def __init__(self):                #constructor
        if(self.instance!=None):
            raise ValueError("a singleton instance is present")

    def setdata(self,num):
        self.num=num
        
    def getdata(self):
        return self.num

obj=Singleton.instance_().setdata(10)
print("the data is= ",Singleton.instance_().getdata())                     
obj1=Singleton()
print(obj1)             #value error shown
print(Singleton.instance_())       #shows the memory address of the singleton object 