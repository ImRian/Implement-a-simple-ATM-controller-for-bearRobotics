class BankSystem:
    def __init__(self):
        # Store user account information
        self.accounts = {
            '1234-5678': {'PIN': '1111', 'balance': 1000},
            '9876-5432': {'PIN': '2222', 'balance': 2000},
        }

    def verify_pin(self, account_number, pin):
        """Check if the account number and PIN match."""
        if account_number in self.accounts and self.accounts[account_number]['PIN'] == pin:
            return True
        return False

    def get_balance(self, account_number):
        """Return the balance of the account."""
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        return None

    def update_balance(self, account_number, amount):
        """Update the balance of the account. Deposit or withdrawal is possible."""
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            return True
        return False

class ATMController:
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.current_account = None

    def insert_card(self, account_number):
        """Simulate card insertion."""
        self.current_account = account_number

    def enter_pin(self, pin):
        """Verify the PIN number."""
        if self.bank_system.verify_pin(self.current_account, pin):
            return True
        else:
            return False

    def select_account(self, account_number):
        """Select an account."""
        self.current_account = account_number

    def check_balance(self):
        """Check the balance of the account."""
        return self.bank_system.get_balance(self.current_account)

    def deposit(self, amount):
        """Deposit money into the account."""
        return self.bank_system.update_balance(self.current_account, amount)

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if self.check_balance() >= amount:
            return self.bank_system.update_balance(self.current_account, -amount)
        else:
            return False