class Bankaccount:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner 
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit successful. New Balance: {self.balance}.")

    def withdrawal(self,amount):
       if amount > self.balance:
           print("Withdrawal unsuccessful. Insufficent balance.")
       else:
           self.balance -= amount
           print(f"Withdrawal successful. New balance: {self.balance}")
        
    def transfer(self,recipient,amount ):
        if amount > self.balance:
            print("Transfer unsuccessful. Insufficent Balance.")
        else:
            self.balance -= amount
            recipient.balance += amount 
            print(f"Transfer successful, New balance: {self.balance}.")


my_account = Bankaccount("123456789", 5678.67, "Colby Hessifer")
brothers_account = Bankaccount("987654321", 7898.88, "Carson Hessifer")

my_account.deposit(500.00)
my_account.withdrawal(2000.00)
my_account.transfer(brothers_account, 500.00)