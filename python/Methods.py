"""class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
        
p=MyClass()
print(MyClass.classmethod())
print(p.classmethod())
#print(p.staticmethod())
#print(p.method())
print(MyClass.classmethod())
print(p.classmethod())
print(MyClass.staticmethod())
print(p.staticmethod())"""


"""class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
        
p=Pizza("tomato")
print(p)
print(Pizza(['cheese', 'tomatoes', " anu "]))
def __repr__(self):
    return 'Pizza(%r)' % self.ingredients
print(Pizza(['mozzarella', 'tomatoes']))
print(Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms']))
print(Pizza(['mozzarella'] * 4))"""




"""import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
        
p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
Pizza(4, ['mozzarella', 'tomatoes'])
print(p.area())
print(Pizza.circle_area(4))"""



"""class anu:
    radius=5
     
    def __init__(self,name):
        self.name=name
        #self.name1=self.names
    

    @classmethod
    def ani(cls,name1):
        cls.radius=50
        cls.name=name1
        return(cls.radius,cls.name)
        
    @classmethod
    def suni(cls):
        return (cls.radius,cls.name)
        
p=anu("anu")
#print(p)
print(p.ani("chinni"))
print(p.suni())
print(p.name)"""



"""class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
        
        
p=Pizza(["cheese","ham"])
print(p)"""



"""class Account:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
list=[]
    
list.append( Account("anu",1))
list.append( Account("anu",2))
list.append( Account("anu",3))
list.append( Account("anu",4))
    
for obj in list: 
    print( obj.name, obj.age, sep =' ' ) """
    
    
    
"""class a:
    def __init__(self,arg1,arg2):
        self.arg1=arg1
        self.arg2=arg2
        
obj=a(1,2)
print(obj.__dict__)

obj.new_argument=10
print(obj.__dict__)


a.arg=10
print(type(a.arg))
print(a.__dict__)"""




"""class a:
    def __init__(self,arg1,arg2):
        self.arg1=arg1
        self.arg2=arg2
        
    def setup(self):
        print(self.arg3)
        
obj=a(1,2)
print(obj.__dict__)
obj.setup()
print(obj.__dict__)"""

class a:
    def __init__(self,arg1,arg2):
        self.arg1=arg1
        self.arg2=arg2
    def setup(self):
        print(self.arg1)
class b(a):
    def __init__(self,name):
        self.name=name        
    def set()
obj=b(1)
print(obj.