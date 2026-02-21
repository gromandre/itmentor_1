class InsufficientFundsError(Exception):
    pass

class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG]: {message}")

class NotificationService:
    def send(self, recipient: str, message: str) -> None:
        print(f"[NOTIFY {recipient}]: {message}")

class FraudDetectionService:
    def is_fraudulent(self, from_user: str, to_user: str, amount: float) -> bool:
        # здесь будет внешний HTTP вызов (условно)
        return False  # допустим, всегда безопасно

class Account:
    def __init__(
        self,
        owner: str,
        balance: float = 0.0,
        logger: Logger | None = None,
        notifier: NotificationService | None = None,
        fraud_checker: FraudDetectionService | None = None,
    ):
        self.owner = owner
        self.balance = balance
        self.logger = logger or Logger()
        self.notifier = notifier or NotificationService()
        self.fraud_checker = fraud_checker or FraudDetectionService()

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.logger.log(f"{self.owner} deposited {amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        self.logger.log(f"{self.owner} withdrew {amount}")

    def transfer(self, target_account: "Account", amount: float) -> None:
        if self.fraud_checker.is_fraudulent(self.owner, target_account.owner, amount):
            self.logger.log("Transfer blocked: fraud detection triggered")
            raise RuntimeError("Fraud detected")
        self.withdraw(amount)
        target_account.deposit(amount)
        self.notifier.send(target_account.owner, f"You received {amount} from {self.owner}")
        self.logger.log(f"{self.owner} transferred {amount} to {target_account.owner}")

    def get_balance(self) -> float:
        return self.balance