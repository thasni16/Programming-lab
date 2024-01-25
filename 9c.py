class bank:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposit amount",amount)
        print("current balance",self.balance)
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print("Withdraw amount",amount)
        print("current balance",self.balance)
account=bank(1234,"Anu","savings",1000)
print("Bank account details")
print("account no:",account.acc_no)
print("name:",account.name)
print("account type:",account.acc_type)
print("balance::",account.balance)
account.deposit(1000)
account.withdraw(500)
