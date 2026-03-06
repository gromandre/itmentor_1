from concurrent.futures import ThreadPoolExecutor
import time
import threading

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self._lock = threading.Lock()

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        with self._lock:
            current = self.__balance
            time.sleep(0.0001)
            self.__balance = current + amount

    def withdraw(self, amount: float):
        with self._lock:
            current = self.__balance
            time.sleep(0.0001)
            self.__balance = current - amount


acc = BankAccount(1000)

with ThreadPoolExecutor(80) as pool:
    pool.map(acc.deposit, [1]*1000)

print(acc.balance)

