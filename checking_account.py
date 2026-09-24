from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit=1000.00):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, target_account):
        if amount > self.transfer_limit:
            print(f"[{self.customer_name}] Transfer denied: ${amount:.2f} exceeds the transfer limit of ${self.transfer_limit:.2f}.")
            return False
        
        print(f"[{self.customer_name}] Attempting transfer of ${amount:.2f} to {target_account.customer_name}...")
        if self.withdraw(amount):
            target_account.deposit(amount)
            print(f"Transfer of ${amount:.2f} to {target_account.customer_name} completed successfully.")
            return True
        else:
            print("Transfer failed: Insufficient funds or minimum balance violated.")
            return False