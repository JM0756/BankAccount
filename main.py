from savings_account import SavingsAccount
from checking_account import CheckingAccount

if __name__ == "__main__":
    print("=== INITIALIZING ACCOUNTS ===")
    # 2 instances of CheckingAccount
    checking1 = CheckingAccount("Alice", 1500.0, 100.0, "CHK-111", "053000219", 500.0)
    checking2 = CheckingAccount("Bob", 800.0, 50.0, "CHK-222", "053000219", 500.0)

    # 2 instances of SavingsAccount
    savings1 = SavingsAccount("Charlie", 5000.0, 500.0, "SAV-333", "053000219", 0.03)
    savings2 = SavingsAccount("Diana", 10000.0, 1000.0, "SAV-444", "053000219", 0.04)

    # Display customer information (shows Bank Title, Protected Acct #, and Routing #)
    print("\n--- Displaying Account Details ---")
    checking1.print_customer_information()
    savings1.print_customer_information()

    # Scenario 1: User opens a checking account and withdraws $x
    print("\n--- SCENARIO 1: Withdrawals from Checking ---")
    print("1a. Valid withdrawal:")
    checking1.withdraw(200.0)

    print("\n1b. Invalid withdrawal (violates minimum balance):")
    checking1.withdraw(1300.0)  # Remaining balance would drop below $100 min balance

    # Scenario 2: Transfer limitation
    print("\n--- SCENARIO 2: Transfer Limitation ---")
    print("2a. Exceeds transfer limit:")
    checking1.transfer(600.0, checking2)  # Fails (over $500 limit)

    print("\n2b. Within transfer limit:")
    checking1.transfer(100.0, checking2)  # Succeeds

    # Scenario 3: Apply interest to savings
    print("\n--- SCENARIO 3: Apply Interest to Savings ---")
    savings1.apply_interest()
    savings2.apply_interest()