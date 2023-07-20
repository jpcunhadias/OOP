from person import Person


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self._owner = owner
        self._balance = balance

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        self._balance = value

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self):
        return f'{self.owner} has {self.balance} in their account'

    def __repr__(self):
        return f'BankAccount({self.owner}, {self.balance})'


if __name__ == '__main__':
    b = BankAccount(Person('Guido', 64), 100.0)
    c = BankAccount(Person('Raymond', 61), 200.0)

    print(b)
    b.deposit(20.0)
    print(b)
    b.withdraw(10.0)
    print(b)
    b.balance = 200.0
    print(b)
    b.transfer(c, 50.0)
    print(b)
    print(c)
