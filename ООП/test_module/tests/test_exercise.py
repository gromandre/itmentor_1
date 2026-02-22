import pytest
from unittest.mock import patch, Mock
from app.exercise import *

def test_log():
    loger = Logger()

    with patch('builtins.print') as mock_print:
        loger.log('message')

    mock_print.assert_called_once_with(f"[LOG]: message")


def test_send():
    service = NotificationService()

    with patch('builtins.print') as mock_print:
        service.send('recipient', 'message')

    mock_print.assert_called_once_with("[NOTIFY recipient]: message")


def test_is_fraudulent_returns_false():
    service = FraudDetectionService()

    result = service.is_fraudulent("A", "B", 100)

    assert result is False

def test_deposit_ok():
    acc = Account("A", 10, logger=Mock())
    acc.deposit(5)
    assert acc.balance == 15

def test_deposit_bad_amount():
    acc = Account("A", 10, logger=Mock())
    with pytest.raises(ValueError):
        acc.deposit(0)

def test_withdraw_ok():
    acc = Account("A", 10, logger=Mock())
    acc.withdraw(3)
    assert acc.balance == 7

def test_withdraw_insufficient():
    acc = Account("A", 10, logger=Mock())
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(20)

def test_transfer_ok():
    fraud = Mock()
    fraud.is_fraudulent.return_value = False

    a = Account("A", 100, logger=Mock(), notifier=Mock(), fraud_checker=fraud)
    b = Account("B", 0,   logger=Mock(), notifier=Mock(), fraud_checker=fraud)

    a.transfer(b, 30)

    assert a.balance == 70
    assert b.balance == 30

def test_transfer_fraud():
    fraud = Mock()
    fraud.is_fraudulent.return_value = True

    a = Account("A", 100, logger=Mock(), notifier=Mock(), fraud_checker=fraud)
    b = Account("B", 0,   logger=Mock(), notifier=Mock(), fraud_checker=fraud)

    with pytest.raises(RuntimeError):
        a.transfer(b, 30)

def test_get_balance():
    acc = Account("A", 42)
    assert acc.get_balance() == 42