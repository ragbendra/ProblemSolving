class ATM:
    def __init__(self,balance=0,pin=0000):
        self.balance = balance
        self.pim = pin
        
    def check_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount>self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return f"Withdrawal successful. Current balance: {self.balance}"
        
        def deposit(self,amount):
            self.balance += amount
            return f"Deposit successful. Current balance: {self.balance}"
        
        def change_pin(self,new_pin):
            self.pin = new_pin
            return f"PIN changed successfully"