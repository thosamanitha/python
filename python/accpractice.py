class Employee:
    raise_amt=1.04


    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+ "."+ last+ "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
         self.pay=int(self.pay*self.raise_amt)
         return self.pay
         
         
         
class developer(Employee):
    
    raise_amt=1.10


    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
    
        
       
class manager(Employee):
        def __init__(self,first,last,pay,employees=None):
           super().__init__(first,last,pay)
           if(employees is None):
             self.employees=[]
           else:
             self.employees=employees
            
        def add_emp(self,emp):
            if(emp not in self.employees):
               self.employees.append(emp)
        
        
        def remove_emp(self,emp):
            if(emp in self.employees):
               self.employees.remove(emp)
             
        
        def print_emp(self):
            for emp in self.employees:
                print("-->", emp.fullname())
        
dev_1=developer("anu","thosam",50000,"python")
dev_2=developer("chinni","thosam",60000,"java")

mgr_1=manager("anu","chinni",90000,[dev_1])

print(isinstance(mgr_1,manager))
print(issubclass(manager,Employee))

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

#print(dev_1.prog_lang)

#print(dev_1.anitha)









#print(dev_1.first,dev_1.pay)
#print(dev_2.email)
#print(dev_1.fullname())
#print(dev_1.apply_raise())

#d=developer("suni","suji",90000)
#print(d.apply_raise())

print(dev_1.pay)
print(dev_1.apply_raise())
print(dev_1.pay)