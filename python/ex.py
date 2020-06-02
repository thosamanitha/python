"""class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @property
    def full_name(self):
        return self.fname+ " " +self.lname
        
p=person("anitha","thosam")
print(p.full_name)"""


"""class Myclass:
    def __init__(self):
        self.a=1
        self.__b=1
    
    def increment_b(self):
        self.__b+=1 
        return self.__b
    def get_b(self):
        return self.__b
        
p=Myclass()
print(p.a)

#print(p.__b)
print(p.increment_b())
print(p.get_b())
print(p._Myclass__b)"""



"""class Myclass:
    a=10
    b=[]
    def __init__(self):
        self.c=1
x,y=Myclass(),Myclass()
print(x.b,y.b,Myclass.b)
x.b.append(10)
print(x.b,y.b,Myclass.b)
Myclass.b.append(20)
print(x.b,y.b,Myclass.b)"""


"""class parent:
    x=1
    def __init__(self):
        self.y=2
    def hello(self):
        print("Hello from Parent")
        return ("return")
class child(parent):
    z=3
    
p,c=parent(),child()
print(p.x,p.y)
print(parent.x,child.x)
print(c.hello())
print(p.hello())
print(c.z)
print(issubclass(child,parent))
print(isinstance(c,child))
print(isinstance(p,parent))"""


"""class parent:
    x=1
    def __init__(self):
        self.y=2
    def hello(self):
        print("Hello from Parent")
        return ("return")
class child(parent):
    z=3
    def hello(self):
        super().hello()   #super() method to get parent methods
        print("hello from child")
        return ("return")
        
p,c=parent(),child()
print(p.hello())
print(c.hello())"""


class anitha:
    def __init__(self):
        self.c=1
    
class sunitha(anitha):
    #def __init__(self):
        #super().__init__()
        z=4
p,cc=anitha(),sunitha()
print(p.c)
print(cc.z)
print(cc.c)
