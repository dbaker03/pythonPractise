class Budget:
    def __init__(self, name: str = "", initial_deposit: int = 0):
        self.name = name,
        self._balance = initial_deposit

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        if self._balance < 0:
            print(f"{self.name[0]} account now overdrawn")

    def get_balance(self):
        return self._balance

    def transfer_to(self, recipient: "Budget", amount):
        self.withdraw(amount)
        recipient.deposit(amount)

    def transfer_from(self, sender: "Budget", amount):
        sender.withdraw(amount)
        self.deposit(amount)

    def __repr__(self):
        return f"Budget(name={self.name}, balance={self._balance}"

    def __str__(self):
        return f"{self.name[0]}: £{self._balance}"


main_bank = Budget('Main', 1000)
print(main_bank)
insurance = Budget('Insurance', 0)
print(insurance)
insurance.withdraw(50)
print(insurance)
main_bank.transfer_to(insurance, 300)
print(main_bank)
print(insurance)
main_bank.withdraw(500)
print(main_bank)
