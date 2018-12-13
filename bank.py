class account:
    def  __init__(self,initial_balance):
        self.balance=initial_balance
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        if(self.balance-amount < 0):
            return "cannott be withdrawed requested amount"
        else:
            self.balance=self.balance-amount
            return self.balance
class Bank:
    def display(self):
        initial_balance=int(input("Enter balance:"))
        a1=account(initial_balance)
        amount=int(input("Amount to be withdrawn:"))
        print("remaining balance:",a1.withdraw(amount))
        amount=int(input("amount to be deposited:"))
        print("total amount present:",a1.deposit(amount))

b1=Bank()
b1.display()

