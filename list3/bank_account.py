class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


class BankAccount:
    def __init__(self, acc_n: int, bal: float, open_date: Date,
                 client_name: str):
        self.account_number = acc_n
        self.balance = bal
        self.open_date = open_date
        self.client_name = client_name

    def deposit(self, amount: float):
        if amount < 0:
            return
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance or amount < 0:
            return
        self.balance -= amount

    def check_balance(self) -> float:
        return self.balance
