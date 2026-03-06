from concurrent.futures import ThreadPoolExecutor
import time

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        current = self.__balance
        time.sleep(0.0001)
        self.__balance = current + amount

    def withdraw(self, amount: float):
        current = self.__balance
        time.sleep(0.0001)
        self.__balance = current - amount


acc = BankAccount(1000)

with ThreadPoolExecutor(80) as pool:
    pool.map(acc.deposit, [1]*1000)

print(acc.balance)

