import unittest
from atm_controller import ATMController, BankSystem

class TestATMController(unittest.TestCase):
    def setUp(self):
        self.bank_system = BankSystem()
        self.atm_controller = ATMController(self.bank_system)

    def test_atm_controller_corrected(self):
        account_number = '1234-5678'
        wrong_pin = '0000'
        correct_pin = '1111'
        deposit_amount = 500
        withdraw_amount = 200

        # Card insertion and PIN verification process
        self.atm_controller.insert_card(account_number)
        self.assertFalse(self.atm_controller.enter_pin(wrong_pin), "Wrong PIN should fail")
        self.atm_controller.insert_card(account_number)  # Select correct account
        self.assertTrue(self.atm_controller.enter_pin(correct_pin), "Correct PIN should pass")

        # Balance check, deposit, and withdrawal process
        initial_balance = self.atm_controller.check_balance()
        self.atm_controller.deposit(deposit_amount)
        self.atm_controller.withdraw(withdraw_amount)
        final_balance = initial_balance + deposit_amount - withdraw_amount
        self.assertEqual(self.atm_controller.check_balance(), final_balance, "Final balance should be correct")

if __name__ == '__main__':
    unittest.main()
