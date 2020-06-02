class Employee:
    

    def __init__(self,first,last):
        self.first1=first
        self.last1=last
        
    def email(self):
        return "{} {}@email.com".format(self.first1,self.last1)
        
    def fullname(self):
        return "{} {}".format(self.first1,self.last1)
        
    def __str__(self):
        return self.first1

        
        
emp_1=Employee("john","smith")
print(emp_1.email())
emp_1.first1="jim"
print(emp_1.first1)
print(emp_1.email())
print(emp_1.__str__())