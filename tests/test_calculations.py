import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount(0)

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (1, 5, 6),
    (12, 4, 16)
])

def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(5, 7) == 35

def test_divide():
    assert divide(18, 3) == 6

def test_bank_set_initial_amount(bank_account): 
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 0

def testwithdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])

def test_bank_transaction(zero_bank_account,deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)