class user:
    def __init__(self,name,mobile_no,address=""):
        self.name=name
        self.mobile=mobile_no
        self.address=address


class BankAccount:
    def __init__(self,user_details):
        self.account_holder=user_details
        self.generate_account_no()
        self.balance=0
        
    def generate_account_no(self):
        import uuid
        self.account_no=str(uuid.uuid4())
        
        
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient amount")
        else:
            self.balance-=amount
        
u=user("anu","99999999",address="kurnool")
print(u.name,u.mobile,u.address)
b=BankAccount(u)
print(b.account_holder.name,b.account_holder.mobile,b.account_no,b.balance)
b.deposit(100)
print(b.balance)
b.deposit(1000)
print(b.balance)
b.withdraw(500)
print(b.balance)