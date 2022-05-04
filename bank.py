class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def user_info(self):
        print("First name: ", self.first_name)
        print("Last Name: ", self.last_name)

    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

# robert = User("Robert", "Seffens", 38)
# jennifer = User("Jennifer", "Anniston", 53)
# rachel = User("Racheal", "Green", 25)


class BankAccount:
    # class attribute

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            # balance = balance + balance * interest rate
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
            
