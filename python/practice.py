class Bank:
    def __init__(self,age):
        self.age=age
       # self.age1=age1
    def __mul__(self,other):
        return Bank(self.age*other.age)
        
if __name__=="__main__":

    bank=Bank(50)
    bank1=Bank(50)
    bank3=bank*bank1
    print(bank3.age)
        